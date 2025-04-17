from dotenv import load_dotenv
import os 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

load_dotenv()


def scrape_wiki(wiki_url: str, mock:bool = False):

    if mock:
        mock_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(mock_url, timeout=10)
        return response.json()

    response = requests.get(wiki_url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text.strip()

    summary = ""
    content_div = soup.find("div", {"class": "mw-parser-output"})
    if content_div:
        for element in content_div.find_all(["p", "div"], recursive=False):
            if element.name == "p" and element.get_text(strip=True):
                summary += element.get_text(strip=True) + " "
            elif element.get("class") and "toc" in element.get("class"):
                break

    infobox_data = {}
    infobox = soup.find("table", {"class": "infobox"})
    if infobox:
        for row in infobox.find_all("tr"):
            header = row.find("th")
            value = row.find("td")
            if header and value:
                key = header.get_text(strip=True)
                val = value.get_text(strip=True)
                infobox_data[key] = val

    # Extract some main sections
    sections = {}
    current_section = None
    for tag in content_div.find_all(["h2", "p"], recursive=True):
        if tag.name == "h2":
            section_title = tag.text.replace("[edit]", "").strip()
            if any(k in section_title.lower() for k in ["early life", "history",  "career", "adaptations", "personal life", "biography", "legacy", "background","filmography","awards", "overview"]):
                current_section = section_title
                sections[current_section] = ""
        elif tag.name == "p" and current_section:
            sections[current_section] += tag.get_text(strip=True) + " "

    data = {
        "title": title,
        "url": wiki_url,
        "summary": summary.strip(),
        "infobox": infobox_data,
        "sections": sections
    }

    return data



if __name__=="__main__":
    print(
        scrape_wiki(
            wiki_url = 'https://en.wikipedia.org/wiki/Bong_Joon_Ho',
        )
    )