__author__ = 'Fares'

import urllib.request
import linkfinder

'''
The function of the spider is to take a link from the waiting list and connect in the page
and grab all the HTML from that page and throw them into the linkfinder class
and it will make sure that the link isn't crawled already, not in the waiting list
before it saves the link in the crawled file, so we don't crawl the same page twice
'''
class Spider:

    #Class varaibles (shared among all instance)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)
        