# azure_oai_env
import os  
import base64
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-demo")  
subscription_key = os.getenv("AZURE_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

def ai_chat(user_message):
    message_text = [
        {"role":"system","content":"You are an AI assistant that helps people find information."},
        {"role":"user","content":user_message}
    ]

    completion = client.chat.completions.create(
    model=deployment,
    messages=message_text,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False
    )

    return completion

print("Welcome! How can I help you today?")

while True:
    user_message = input(">> ")
    completion = ai_chat(user_message)
    # Completion will return a response that we need to use to get the actual string
    print("AI: " + completion.choices[0].message.content)
