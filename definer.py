import requests
from bs4 import BeautifulSoup
from random import randint


def write_word_file():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    f = open('words.txt', "w")
    for item in WORDS:
        item = str(item)[1:].replace("'", "")
        f.write(item + "\n")
    f.close()


def get_word():
    f = open('words.txt', "r")
    WORDS = f.readlines()
    word = WORDS[randint(0, len(WORDS))]
    word = word.replace("\n", "")

    return word


def definer(word):
    defs = []
    page = requests.get("https://www.ldoceonline.com/dictionary/" + word)
    soap = BeautifulSoup(page.content, "html.parser")
    text = soap.find_all(class_="DEF")[:3]
    for count, item in enumerate(text):
        defs.append(str(count + 1) + ". " + item.get_text().strip())
    return defs