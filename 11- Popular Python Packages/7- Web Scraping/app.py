from urllib import response
import requests
from bs4 import BeautifulSoup as parse

response = requests.get("https://stackoverflow.com/questions")
# print(response)
content = parse(response.text, "html.parser")
# print(content)
questions = content.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").get_text())
    print(question.select_one(".vote-count-post").get_text())
