# 代码生成时间: 2025-08-12 01:49:36
import scrapy
import requests
from scrapy.utils.response import response_status_message
from scrapy.exceptions import NotConfigured
from scrapy.utils.python import to_bytes
from scrapy.spiders import Spider
from urllib.parse import urlparse
from scrapy.http import Request



class URLValidator(Spider):
    '''
    A Scrapy Spider for validating the validity of URLs.
    '''
    name = 'url_validator'
    allowed_domains = ['*']  # Allow all domains
    start_urls = ['http://example.com', 'https://www.google.com']  # Starting URLs

    def parse(self, response):
        '''
        Parse the response and yield a new Request for each URL found.
        '''
        # Check if the URL is valid
        if response.status == 200 and urlparse(response.url).scheme in ['http', 'https']:
            self.log(f'URL {response.url} is valid.')
        else:
            self.log(f'URL {response.url} is invalid.')

    def verify_url(self, url):
        '''
        Verify the validity of a given URL.
        '''
        if not url:
            raise ValueError('URL cannot be empty.')

        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code == 200
        except requests.RequestException as e:
            self.log(f'Error verifying URL {url}: {e}')
            return False

    def start_requests(self):
        '''
        Start the scraping process by yielding a Request for each URL in start_urls.
        '''
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

# Usage:
# scrapy crawl url_validator