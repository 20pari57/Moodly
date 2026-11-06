import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face API token not found!")

# Initialize DeepSeek model
model = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    base_url="https://router.huggingface.co/v1",
    api_key=hf_token,
    max_tokens=512,
    temperature=0.7
)

# Ask a question
response = model.invoke(
    "Who wrote the national anthem of India?"
)

print(response.content)
