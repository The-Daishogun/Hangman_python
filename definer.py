import urllib3
import re

from bs4 import BeautifulSoup


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def find(word):
    url = "https://www.thefreedictionary.com/" + word
    req = urllib3.PoolManager()
    result = req.request("GET", url)
    soup = BeautifulSoup(result.data, 'html.parser')
    content = soup.find_all(class_='ds-list')
    content = cleanhtml(str(content[0])).replace(":", "")
    content = content.lstrip()

    if content[0].isnumeric():
        content = content[2:]

    return content.lstrip()


def debug():
    a = input()
    print(find(a))


