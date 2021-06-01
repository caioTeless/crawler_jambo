"""
def search_wikpedia(url='https://pt.wikipedia.org/wiki/', topic=''):
    req = requests.get(url + topic)
    bs = BeautifulSoup(req.text, 'html.parser')
    title = bs.find('h1').text
    lines = bs.find_all(('p', {'class': 'mw-content-text'}))
    body = ''.join([line.text for line in lines])
    content = Content('', url, title, body)
    return content.print()
"""


class WikiContent:

    def __init__(self, url='', content=''):
        self.url = url
        self.content = content

    def return_content(self):
        return self.content

    def return_urls(self):
        return self.url
