from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from better_profanity import profanity

app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
profanity.load_censor_words()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    thread_text = data.get("thread_text", "")
    comments = data.get("comments", [])

    flagged_comments = []

    for comment in comments:
        is_toxic = profanity.contains_profanity(comment)

        flagged_comments.append({
            "comment": comment,
            "toxic": is_toxic
        })

    toxic_count = sum(
        1 for c in flagged_comments if c["toxic"]
    )

    safe_count = len(comments) - toxic_count
    toxicity_percentage = round(
    (toxic_count / len(comments)) * 100,
    2
    )

    if len(comments) == 0:
        return jsonify({
    "analysis": response_text,
    "flagged": flagged_comments,
    "sentiment": sentiment,
    "total_comments": len(comments),
    "toxic_comments": toxic_count,
    "safe_comments": safe_count,
    "toxicity_percentage": toxicity_percentage
    })

    prompt = f"""
Analyze the following discussion.

Thread:
{thread_text}

Comments:
{comments}

Provide:

Summary:
(2-3 sentences)

Sentiment:
(Positive / Negative / Neutral)

Key Topics:
(2-3 bullet points)
"""

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)

        import re

        response_text = response.text

        sentiment = "Unknown"

        match = re.search(
            r"Sentiment.*?\n\s*(Positive|Negative|Neutral)",
            response_text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            sentiment = match.group(1)

        return jsonify({
            "analysis": response_text,
            "flagged": flagged_comments,
            "sentiment": sentiment,
            "total_comments": len(comments),
            "toxic_comments": toxic_count,
            "safe_comments": safe_count
        })

    except Exception as e:
        return jsonify({
            "analysis": f"Gemini Error: {str(e)}",
            "flagged": flagged_comments,
            "sentiment": "Unknown",
            "total_comments": len(comments),
            "toxic_comments": toxic_count,
            "safe_comments": safe_count
        })


if __name__ == "__main__":
    app.run(debug=True)