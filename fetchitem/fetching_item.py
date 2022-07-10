import requests
from bs4 import BeautifulSoup

allhtml = []
def fetchallHTML():
    before_url = "https://distrowatch.com/table.php?distribution="
    html = open("word.txt", "r", encoding='utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find_all("td", class_="phr2"):
        item = requests.get(before_url + i.find('a').getText()).text
        print(item)
        allhtml.append(item)

def proccessHTML()
# fetchallHTML()
allhtml.append(open("testing.html", "r", encoding='utf-8'))


