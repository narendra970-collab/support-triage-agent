import os
import json
from ssl import OPENSSL_VERSION
from sys import api_version
from dotenv import load_dotenv
from openai import AzureOpenAI
from prompt import SYSTE_PROMPT

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def run_agent(user_message: str):
    
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": SYSTE_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0.2
    )
    raw_response = response.choices[0].message.content
    return raw_response


if __name__ == "__main__":
    user_message = "Login fails with 401 error after password reset"
    response = run_agent(user_message)
    print("\nAgent Response:\n")
    print(response)