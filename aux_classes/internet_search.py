import os
import re
import sys

import requests
from bs4 import BeautifulSoup
from googlesearch import search
from aux_classes import wikipedia_cll
from helpers import crawler_header, helper_message_box


class InternetSearch:
    site_tips = set()
    site_caught = set()

    def __init__(self, query='', cont=0):
        self.query = query
        self.cont = cont

    def get_pages_wikipedia(self):
        sites = set()
        with open('data.txt', 'w+', encoding='utf-8') as my_data:
            try:
                for searchs in search(self.query, lang='pt-BR', num=self.cont, stop=self.cont, pause=5):
                    sites.add(searchs)
                    self.site_tips.add(searchs)
                for site in sites:
                    html = requests.get(site, headers=crawler_header.headers)
                    bs = BeautifulSoup(html.text, 'html.parser')
                    if 'https://pt.wikipedia.org/wiki/' in site:
                        self.site_caught.add(site)
                        self.site_tips.discard(site)
                        lines = bs.find_all(('p', {'class': 'mw-content-text'}))
                        body = ''.join([line.text for line in lines])
                        wiki = wikipedia_cll.WikiContent(content=body)
                        format_data = re.sub('\[(.*?)\]', '',
                                             wiki.return_content())  # remove citações no final de cada '.'
                        my_data.writelines(format_data)
            except Exception:
                return False
        return True

    def read_pages(self):
        with open('data.txt', 'r', encoding='utf-8') as my_data:
            return my_data.readlines()

    """
    def get_page_blogs(self):
        sites = []
        my_craw = crawler.Crawler()
        for row in site_data.siteData:
            sites.append(web_site_model.Website(row[0], row[1], row[2], row[3],
                                                row[4], row[5], row[6], row[7]))

        topics = ['história do paraguai', 'história do brasil']
        lista_content = []
        for topic in topics:
            for target_site in sites:
                lista_content.append(my_craw.search(topic, target_site))
        return lista_content
    """
