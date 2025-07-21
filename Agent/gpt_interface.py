# Agent/gpt_interface.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful DevOps assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
