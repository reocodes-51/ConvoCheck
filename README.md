# ConvoCheck

ConvoCheck is an AI-powered web application that generates concise summaries of conversations while also detecting toxic content within chats. It helps users quickly understand lengthy discussions and promotes safer online communication by identifying inappropriate language.

## 🚀 Features

* **AI-Powered Chat Summarization** using Google's Gemini 1.5 Flash model.
* **Toxicity Detection** using the local `profanity` library.
* **Interactive User Interface** built with HTML, CSS, and JavaScript.
* **Fast Backend Processing** powered by Flask and Python.
* **Real-Time Analysis** of user-provided conversations.

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Flask (Python)

### AI & NLP

* Google Gemini 1.5 Flash API
* Profanity Library

## 📂 Project Structure

```text
ConvoCheck/
│
├── static/          # CSS, JavaScript, and assets
├── templates/       # HTML templates
├── app.py           # Flask backend
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ConvoCheck.git
cd ConvoCheck
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

## 🎯 How It Works

1. Enter or paste a conversation into the application.
2. The Gemini API generates a concise summary of the chat.
3. The toxicity detection module scans the conversation for offensive or inappropriate language.
4. Results are displayed through an easy-to-use web interface.

## 👥 Team Alpha Next

This project was developed collaboratively by:

* **Bhavya Vaish**
* **Rajyavardhan Singh Rathore**
* **Sharad Gupta**

## ⭐ Support

If you found this project useful, consider giving the repository a **Star ⭐** on GitHub.

