__author__ = 'Fares'

import html.parser
import urllib

'''
The function of this class is to parse through all the HTML page and grab all the links
'''


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super(self).__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set

    # when we call HTMLParser feed(), this function is called when it encounters an opening tag<a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
