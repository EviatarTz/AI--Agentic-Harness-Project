import sys 
import openai

sys.stdout.reconfigure(encoding = 'utf-8') #so emojis don't crush the windows console 

from openai import OpenAI

# One client. Point it at any OpenAI compatible server(Ollama here)
client = OpenAI(base_url = "http://localhost:11434/v1",api_key = "ollama")
MODEL = "qwen3.5:4b"

def chat(user_message: str) -> str:
    response = client.chat.completions.create(
        model = MODEL,
        message = [
            {"role": "system", "content" :"You are a helpful personal assistant."},
            {"role": "user", "content": user_message},  
        ],
    )
    return response.choices[0].message.content or ""

if __name__ == "__main__":
    print(f"v0 assistant ({MODEL}) - cmd + c to quit")
    try:
        while True:
            question = input("\nyou: ")
            print("\nassistant:" , chat(question))
    except(EOFError, KeyboardInterrupt):
        print("\nbye!")

