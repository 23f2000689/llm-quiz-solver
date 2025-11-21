from bs4 import BeautifulSoup

def extract_answer(html):
    soup = BeautifulSoup(html, "html.parser")

    question = soup.find("h1").text if soup.find("h1") else "No question"
    options = [li.text for li in soup.find_all("li")]
    context = soup.find("p").text if soup.find("p") else None

    return {
        "question": question,
        "options": options,
        "context": context
    }
