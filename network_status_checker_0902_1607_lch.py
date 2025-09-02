# 代码生成时间: 2025-09-02 16:07:19
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings
from scrapy.utils.python import to_bytes
import requests
from urllib.parse import urlparse

"""
Network Status Checker using Python and Scrapy framework.
Checks the network connection status by pinging a list of URLs.
"""


class NetworkStatusChecker(scrapy.Spider):
    def __init__(self, urls=None, *args, **kwargs):
        """
        Initializes the Spider with a list of URLs to check.
        :param urls: List of URLs to check for connection status.
        """
        super(NetworkStatusChecker, self).__init__(*args, **kwargs)
        self.urls = urls or []
        self.settings = get_project_settings()

    def start_requests(self):
        """
        Generate requests for each URL to check.
        """
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Check the response status for each URL.
        If the status code is 200, the URL is considered reachable.
        """
        url = response.url
        if response.status == 200:
            self.log(f'Successfully connected to {url}')
        else:
            self.log(f'Failed to connect to {url}. Status: {response.status}', level=logging.ERROR)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """
        Create an instance from a Scrapy crawler.
        :param crawler: The Scrapy crawler instance.
        """
        return super(NetworkStatusChecker, cls).from_crawler(crawler, *args, **kwargs)


# Function to add custom settings to the Scrapy project
def setup_crawler(crawler):
    crawler.settings.set('USER_AGENT', 'NetworkStatusChecker (+http://example.com/)')
    crawler.settings.set('FEED_FORMAT', 'json')
    crawler.settings.set('FEED_URI', 'results.json')

# Main function to run the Scrapy spider
def run_spider(urls):
    try:
        process = CrawlerProcess(get_project_settings())
        # Set up the crawler
        process.crawl(NetworkStatusChecker, urls=urls)
        process.start()
    except NotConfigured as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # List of URLs to check
    urls_to_check = [
        'http://www.google.com',
        'http://www.example.com',
        'http://nonexistentwebsite1234.com'
    ]
    # Run the spider
    run_spider(urls_to_check)