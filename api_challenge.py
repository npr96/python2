import requests
from bs4 import BeautifulSoup


def link_scraper(link):
    api_string = requests.get(link)
    api_string = api_string.text
    formatted_string = BeautifulSoup(api_string, 'html.parser')
    for link in formatted_string.find_all('a'):
        if 'data-turbolinks="false"' in str(link).split():
            print(link.get_text())
        else:
            pass


link_scraper('http://www.dailysmarty.com/topics/python')
