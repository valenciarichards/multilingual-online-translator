import requests

from bs4 import BeautifulSoup

act_number = int(input())
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")
print(links[act_number - 1]["href"])
