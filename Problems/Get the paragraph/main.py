import requests

from bs4 import BeautifulSoup

word = input()
link = input()

response = requests.get(link)
soup = BeautifulSoup(response.text)

paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    if word in paragraph.text:
        print(paragraph.text)
        break
