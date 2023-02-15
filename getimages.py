#get image links
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as b



# Original headers from classcentral
head = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

url = Request('https://www.classcentral.com/', headers=head)
page = urlopen(url)

soup = b(page, "lxml")
# print(soup)

for link in soup.find_all('img'):
    print(link)