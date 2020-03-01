import requests
import bs4
import os

BASR_URL = "https://tuoitre.vn"
SOURCE_URL = "https://tuoitre.vn/tin-moi-nhat.htm"


def getArticle(link):

    r = requests.get(link["url"])
    r = bs4.BeautifulSoup(r.content, features="html.parser")
    body = r.select_one("#main-detail-body")
    title = r.select_one(".article-title").text
    return ({
        "id": link["id"],
        "title": title,
        "body": body
    })


def getListArticle():
    r = requests.get(SOURCE_URL)
    links = []
    if r.ok:
        content = bs4.BeautifulSoup(r.content, features="html.parser")
        a = content.select(".title-news > a")
        for link in a:
            links.append({
                "id": link["data-id"],
                "url": BASR_URL + link["href"],
                "title": link.text
            })
    else:
        print("Error when go to " + SOURCE_URL)
    return links

