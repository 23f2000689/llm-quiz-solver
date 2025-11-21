import requests
from extractor import extract_answer
from solver import solve_quiz

async def solve_quiz_chain(email, secret, url):
    page_text = requests.get(url).text
    extracted = extract_answer(page_text)
    llm_answer = solve_quiz(extracted["question"], extracted["options"], extracted["context"])
    print("Solved:", llm_answer)
