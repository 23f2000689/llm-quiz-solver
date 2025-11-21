import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def solve_quiz(question: str, options=None, context=None):
    prompt = f"""
Answer the question clearly.

Question: {question}
Options: {options}
Context: {context}

Give only final answer.
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content
