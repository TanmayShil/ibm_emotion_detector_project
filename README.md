# Emotion Detection Web Application

An AI-powered Emotion Detection Web Application built using Python, Flask, and IBM Watson NLP APIs. The application analyzes user-provided text and detects emotions such as Joy, Anger, Fear, Sadness, and Disgust, while identifying the dominant emotion.

## 🚀 Features

- Detects multiple emotions from text input
- Identifies the dominant emotion
- Interactive web interface using Flask
- Real-time emotion analysis
- REST API integration with IBM Watson NLP
- Error handling for invalid inputs
- Unit testing support
- Clean and modular project structure

---

## 🛠️ Technologies Used

- Python
- Flask
- IBM Watson NLP API
- HTML5
- JavaScript
- Requests Library
- UnitTest

---

## 📂 Project Structure

```bash
EmotionDetectionProject/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/emotion-detection-app.git
cd emotion-detection-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python server.py
```

Application will be available at:

```bash
http://localhost:5000
```

---

## 🧪 Running Unit Tests

```bash
python -m unittest test_emotion_detection.py
```

---

## 📸 Application Workflow

1. Enter text into the input field.
2. Click **Analyze Emotion**.
3. The application sends the text to the IBM Watson Emotion Detection API.
4. Emotion scores are returned.
5. The dominant emotion is displayed to the user.

---

## Example Output

Input:

```text
I am extremely happy today!
```

Output:

```text
For the given statement, the system response is:
anger: 0.01
disgust: 0.02
fear: 0.03
joy: 0.92
sadness: 0.02

The dominant emotion is joy.
```

---

## 📚 Learning Outcomes

This project demonstrates:

- Python package development
- Flask web application development
- API integration
- Natural Language Processing (NLP)
- Software testing
- Modular application architecture
- Backend development best practices

---

## 🎓 IBM Skills Network Project

This project was completed as part of the IBM course:

**Developing AI Applications with Python and Flask**

Offered by IBM through Coursera and IBM Skills Network.

---

## 👨‍💻 Author

**Tanmay Shil**

Full Stack Developer (MERN Stack)

### Skills

- React.js
- Next.js
- TypeScript
- JavaScript
- Node.js
- Express.js
- MongoDB
- Redux Toolkit
- Material UI
- Python
- Flask

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
