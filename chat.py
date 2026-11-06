from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9,max_tokens=120) # Gemini model
response = model.invoke("can u write down a hacker poem?")
print(response.content)