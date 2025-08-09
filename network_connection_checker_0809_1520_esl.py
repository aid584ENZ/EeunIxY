# 代码生成时间: 2025-08-09 15:20:38
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
import requests
from urllib.parse import urlparse

"""
A Scrapy Spider to check network connection status.
This script uses Scrapy framework to check if a given URL
is reachable and returns its response status code.
"""

class NetworkConnectionSpider(scrapy.Spider):
    '''
    A Scrapy Spider to check network connection status.
    It attempts to fetch a URL and checks for a successful response.
    '''
    name = 'network_connection_checker'
    start_urls = []  # List to hold URLs to check

    def __init__(self, urls=None, *args, **kwargs):
        super(NetworkConnectionSpider, self).__init__(*args, **kwargs)
        if urls is None:
            urls = []
        self.start_urls = urls

    def parse(self, response):
        """
        This method is called to handle the response downloaded for each of the
        start URLs. Here we check the response status code and yield it.
        """
        self.log(f"URL: {response.url} returned status: {response.status}")
        yield {
            'url': response.url,
            'status': response.status
        }

    def check_url(self, url):
        """
        Helper method to check if a URL is reachable.
        It uses the requests library to make a HEAD request to the URL.
        If the URL is reachable, it will be added to the start_urls.
        """
        try:
            response = requests.head(url, timeout=10)
            if response.status_code == 200:
                self.start_urls.append(url)
        except requests.RequestException as e:
            self.log(f"Failed to connect to {url}: {e}")

    def start_requests(self):
        """
        This method is called to start the scraping process.
        It checks each URL to see if it's reachable and yields a Request
        for each reachable URL.
        """
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


# Function to run the spider with a list of URLs
def run_spider(urls):
    process = CrawlerProcess()
    try:
        # Add the spider to the process
        process.crawl(NetworkConnectionSpider, urls=urls)
        # Start the crawling process
        process.start()
    except NotConfigured as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    urls_to_check = [
        "http://www.example.com",
        "https://nonexistentwebsite1234.com"
    ]
    run_spider(urls_to_check)