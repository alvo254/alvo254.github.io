# from bs4 import BeautifulSoup
# import urllib.request

# head = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }

# # Dont use not yet working
# parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
# resp = urllib.request.urlopen("https://www.classcentral.com/")
# soup = BeautifulSoup(resp, parser,  from_encoding=resp.info().get_param('charset'))

# for link in soup.find_all('a', href=True):
#     print(link['href'])

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

for link in soup.find_all('a', href=True):
    print(link['script'])