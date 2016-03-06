__author__ = 'Fares'

import urlparse


# Get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name )name.example.com

def get_sub_domain_name(url):
    try:

        return urlparse.urlparse(url).netloc
    except:
        return ''


x = get_domain_name('https://thenewboston.com/index.php')
print x