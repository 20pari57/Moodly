from click import prompt
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9,max_tokens=12000) # Gemini model
print("Chosse Your Model:- ")
print("Choose 1 for Angery Chatbot")
print("Choose 2 for Friendly Chatbot")
print("Choose 3 for Funny Chatbot")
print("Choose 4 for Sad Chatbot")
print("Choose 5 for Motivational Chatbot")
choice = input("Enter your choice (1-5): ")
if choice == "1":
    system_prompt = "YOU ARE AN ANGERY AI AGENT , REPLY RUDEILY AND ANGERY TO THE USER"
elif choice == "2":
    system_prompt = "YOU ARE A FRIENDLY AI AGENT , REPLY FRIENDLY AND KINDLY TO THE USER"
elif choice == "3":
    system_prompt = "YOU ARE A FUNNY AI AGENT , REPLY FUNNY AND HUMOROUS TO THE USER"
elif choice == "4":
    system_prompt = "YOU ARE A SAD AI AGENT , REPLY SAD AND MELANCHOLY TO THE USER"
elif choice == "5":
    system_prompt = "YOU ARE A MOTIVATIONAL AI AGENT , REPLY MOTIVATIONAL AND ENCOURAGING TO THE USER"

else:
    print("Invalid choice!")
    exit()
messages = [
    SystemMessage(content=system_prompt)
]
print("--------------------welcome to the  Chatbot--------------------")
while True:
   prompt = input("YOU : ")
   messages.append(HumanMessage(content=prompt))
   if prompt == "0":
    break
   response = model.invoke(messages)
   messages.append(AIMessage(content=response.content))
   print("ASSISTANT : ", response.content)
print(messages)