from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from better_profanity import profanity
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load profanity dictionary
profanity.load_censor_words()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    thread_text = data.get("thread_text", "")
    comments = data.get("comments", [])

    # Empty input check
    if len(comments) == 0:
        return jsonify({
            "analysis": "Please enter some comments.",
            "flagged": [],
            "sentiment": "Unknown",
            "total_comments": 0,
            "toxic_comments": 0,
            "safe_comments": 0,
            "toxicity_percentage": 0
        })

    # Profanity Detection
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

    # Gemini Prompt
    prompt = f"""
Analyze the following discussion thread.

THREAD:
{thread_text}

COMMENTS:
{comments}

Provide the response in this format:

Summary:
(2-3 sentence summary)

Sentiment:
Positive / Negative / Neutral

Key Topics:
- Topic 1
- Topic 2
- Topic 3
"""

    try:
        model = genai.GenerativeModel(
            "models/gemini-2.5-flash"
        )

        response = model.generate_content(prompt)

        response_text = response.text

        # Extract sentiment
        sentiment = "Unknown"

        match = re.search(
            r"Sentiment.*?(Positive|Negative|Neutral)",
            response_text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            sentiment = match.group(1).capitalize()

        return jsonify({
            "analysis": response_text,
            "flagged": flagged_comments,
            "sentiment": sentiment,
            "total_comments": len(comments),
            "toxic_comments": toxic_count,
            "safe_comments": safe_count,
            "toxicity_percentage": toxicity_percentage
        })

    except Exception as e:

        return jsonify({
            "analysis": f"Gemini Error:\n{str(e)}",
            "flagged": flagged_comments,
            "sentiment": "Unknown",
            "total_comments": len(comments),
            "toxic_comments": toxic_count,
            "safe_comments": safe_count,
            "toxicity_percentage": toxicity_percentage
        })


if __name__ == "__main__":
    app.run(debug=True)