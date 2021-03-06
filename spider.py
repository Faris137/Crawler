__author__ = 'Fares'

import urlopen
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
        Spider.queue = general.file_to_set(Spider.queue_file)
        Spider.crawled = general.file_to_set(Spider.crawled_file)


    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()


    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_type = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: page cannot be crawled')
            return set()
        return finder.page_links()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)


    @staticmethod
    def update_files():
        general.set_to_file(Spider.queue, Spider.queue_file)
        general.set_to_file(Spider.crawled, Spider.crawled_file)
