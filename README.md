# Moodly 💬

**A chatbot with moods.** Pick how you want it to talk to you: angry, friendly, funny, sad, or motivational. Then just start chatting.

I built Moodly while learning Generative AI. It started as a simple terminal chatbot in Python, and I turned it into a proper web app with a clean, soft-colored interface.

---

## What it does

- Lets you choose from **5 chatbot personalities**:
  - 😠 **Angry**: rude and fired up
  - 😊 **Friendly**: warm and kind
  - 😂 **Funny**: jokes and humour
  - 😢 **Sad**: soft and melancholy
  - 💪 **Motivational**: pep talks and encouragement
- Remembers the conversation, so the bot knows what you said earlier
- Starts a fresh chat when you switch moods or press **Clear chat**
- Works in the browser with a responsive layout (desktop and mobile)

---

## How it works

The browser can't run Python directly, so there are two parts that talk to each other:

```
Browser (HTML / CSS / JS)  →  Flask server (Python)  →  Groq AI model
        your chat page            server.py              via LangChain
```

1. You type a message on the web page.
2. `script.js` sends it to the Flask server.
3. `server.py` adds your mood's system prompt and the chat history, and asks the AI model for a reply.
4. The reply travels back and shows up in the chat.

---

## Tech used

- **Python 3**
- **Flask** and **Flask-CORS** for the small web server
- **LangChain** with **Groq** (`openai/gpt-oss-120b`) for the AI
- **HTML, CSS and JavaScript** for the interface
- **python-dotenv** to keep the API key private

---

## Project structure

```
chatmodels/
├── server.py      # Flask server + AI logic
├── index.html     # The page
├── style.css      # Styling
├── script.js      # Chat behaviour, talks to the server
├── .env           # Your secret API key (never share this)
└── README.md
```

---

## Getting started

### 1. Clone or download the project

```bash
cd chatmodels
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, use `venv\Scripts\activate` instead.

### 3. Install the packages

```bash
pip install flask flask-cors python-dotenv langchain langchain-groq
```

### 4. Add your API key

Create a file named `.env` in the project folder and add your Groq key:

```
GROQ_API_KEY=your_key_here
```

You can get a free key from [console.groq.com](https://console.groq.com).

> **Important:** never upload your `.env` file to GitHub. Add `.env` to your `.gitignore`.

### 5. Start the server

```bash
python3 server.py
```

You should see:

```
Starting server on http://127.0.0.1:5001 ...
 * Running on http://127.0.0.1:5001
```

Keep this terminal open while you use the app.

### 6. Open the page

Open `index.html` with **Live Server** in VS Code (or any local server). Pick a mood and start chatting!

---

## Troubleshooting

| Problem | What to try |
|---|---|
| The terminal prints nothing and returns to the prompt | `server.py` may be empty or unsaved. Run `wc -l server.py` and check it has about 57 lines. |
| Chat says "Cannot reach the server" | Make sure `python3 server.py` is running, and the port in `script.js` (`5001`) matches. |
| Chat says "The AI model failed" | Check the server terminal for the error. Usually the `GROQ_API_KEY` in `.env` is missing or wrong. |
| Nothing changes after editing `script.js` | Hard refresh the page with Cmd+Shift+R (Ctrl+Shift+R on Windows). |
| Port 5000 errors on Mac | That port is used by AirPlay. This project already uses 5001 to avoid it. |

---

## Ideas for the future

- Stream the reply word by word, like ChatGPT
- Save chat history to a file or database
- Add more moods (sarcastic, pirate, poetic...)
- Deploy it online so anyone can try it

---

## What I learned

- How to give an AI a personality using system prompts
- How to keep conversation memory with LangChain messages
- How to connect a Python backend to a JavaScript frontend with an API
- Why CORS exists, and how to deal with it

---

Made with curiosity and a lot of debugging ☕
