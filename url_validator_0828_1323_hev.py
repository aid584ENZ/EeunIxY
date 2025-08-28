# 代码生成时间: 2025-08-28 13:23:49
import scrapy
def validate_url(url):
    """
    Validate the given URL.

    Args:
    url (str): The URL to validate.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """
    try:
        response = scrapy.Request(url=url, callback=lambda response: True)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return True
    except (scrapy.exceptions.NotSupported, scrapy.exceptions.TimeoutError,
            requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        return False

class UrlValidatorSpider(scrapy.Spider):
    name = 'url_validator'
    allowed_domains = []
    start_urls = []

    def __init__(self, start_urls=None, *args, **kwargs):
        super(UrlValidatorSpider, self).__init__(*args, **kwargs)
        self.start_urls = start_urls or []

    def parse(self, response):
        # This method will be called for each start URL
        if validate_url(response.url):
            self.log(f'URL {response.url} is valid.')
        else:
            self.log(f'URL {response.url} is invalid.', level=logging.ERROR)

# Usage example
if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    start_urls = [
        'https://www.example.com',
        'http://invalid-url.com',
    ]

    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(UrlValidatorSpider, start_urls=start_urls)
    process.start()