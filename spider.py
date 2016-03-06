__author__ = 'Fares'

import urllib.request
import linkfinder
import general

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


    # in booting when the first spider work then it has to create the project folder and it's files the list and queue
    @staticmethod
    def boot():
        general.create_project_dir(Spider.project_name)
        general.create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = general.file_to_set(Spider, Spider.queue_file)
        Spider.crawled = general.file_to_set(Spider,Spider.crawled_file)