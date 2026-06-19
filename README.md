# ConvoCheck

ConvoCheck is an **AI-powered web application** that generates summaries of input chats while also detecting toxicity within conversations. It provides users with concise, meaningful insights from long discussions, making online communication more effective and safe.

---

## 🚀 Features

* **Chat Summarization** using Google Gemini `gemini-1.5-flash` API.
* **Toxicity Detection** powered by the `profanity` library running locally.
* **Interactive Web Interface** built with HTML, CSS, and JavaScript.
* **Backend Processing** powered by Flask and Python.

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **AI Model:** Google `gemini-1.5-flash` API
* **Toxicity Detection:** Profanity library (local)

---

## 📂 Project Structure

```
ConvoCheck/
│── static/        # CSS, JS, Images
│── templates/     # HTML templates
│── app.py         # Flask backend
│── requirements.txt
│── README.md
```

---

## 👥 Team Alpha Next
Bhavya Vaish, Rajyavardhan Singh Rathore ,Sharad Gupta
---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-repo>/ConvoCheck.git
   cd ConvoCheck
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your Google Gemini API key to the project (e.g., in `.env` file).

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open the app in your browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 📜 License

This project is developed by **Team Alpha Next**. Feel free to use and modify with proper attribution.

---

## 🌟 Future Enhancements

* Multi-language support for summarization.
* Advanced toxicity classification.
* Export summaries in PDF/Docx.
* Real-time chat summarization.# ConvoCheck
