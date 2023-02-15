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
    print(link['href'])

# print(links)


# HEADERS = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Cache-Control": "max-age=0",
#     }

r = requests.get('https://www.classcentral.com/', headers=head)
# pipe this into a html file and get the whole website
# print(r.text)



# soup = b(web, "html.parser")
# print(soup)


# soup = b(r.content)
# print(soup.prettify())

# link = soup.select('a')
# print(link)


