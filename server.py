from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

app = Flask(__name__)
CORS(app)  # lets the page from Live Server call this server

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0.9, max_tokens=12000)

# keys match the mood ids used in script.js
PROMPTS = {
    "angry": "YOU ARE AN ANGERY AI AGENT , REPLY RUDEILY AND ANGERY TO THE USER",
    "friendly": "YOU ARE A FRIENDLY AI AGENT , REPLY FRIENDLY AND KINDLY TO THE USER",
    "funny": "YOU ARE A FUNNY AI AGENT , REPLY FUNNY AND HUMOROUS TO THE USER",
    "sad": "YOU ARE A SAD AI AGENT , REPLY SAD AND MELANCHOLY TO THE USER",
    "motivational": "YOU ARE A MOTIVATIONAL AI AGENT , REPLY MOTIVATIONAL AND ENCOURAGING TO THE USER",
}

histories = {}  # one conversation per mood


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    mood = data.get("mood", "friendly")

    if mood not in PROMPTS:
        return jsonify({"error": "Invalid mood"}), 400
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if mood not in histories:
        histories[mood] = [SystemMessage(content=PROMPTS[mood])]
    messages = histories[mood]

    messages.append(HumanMessage(content=user_message))
    try:
        response = model.invoke(messages)
    except Exception as e:
        messages.pop()  # remove the failed user message
        print("Model error:", e)
        return jsonify({"error": "The AI model failed. Check the server terminal."}), 500
    messages.append(AIMessage(content=response.content))

    return jsonify({"reply": response.content})


@app.route("/reset", methods=["POST"])
def reset():
    mood = (request.get_json() or {}).get("mood", "friendly")
    histories.pop(mood, None)
    return jsonify({"ok": True})


if __name__ == "__main__":
    print("Starting server on http://127.0.0.1:5001 ...")
    app.run(host="127.0.0.1", port=5001, debug=True)