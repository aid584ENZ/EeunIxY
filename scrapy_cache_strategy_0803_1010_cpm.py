# 代码生成时间: 2025-08-03 10:10:59
import scrapy


class CacheSpider(scrapy.Spider):
    name = 'cache_spider'
    allowed_domains = ['example.com']  # Replace with your target site
    start_urls = ['http://example.com/']  # Replace with your target URL

    custom_settings = {
        'HTTPCACHE_STORAGE': 'scrapy.extensions.httpcache.FilesystemCacheStorage',
        'HTTPCACHE_EXPIRATION_SECS': 0,  # Cache forever
        'HTTPCACHE_DIR': 'httpcache',
        'HTTPCACHE_IGNORE_HTTP_CODES': [],
        'HTTPCACHE_POLICY': 'scrapy.extensions.httpcache.RFC2616Policy',
        'HTTPCACHE_CHECK_IGNORE': []
    }

    def start_requests(self):
        """
        Start requests using cache policy.
        """
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.handle_error)

    def parse(self, response):
        """
        Parse the response and extract data.
        """
        # Extract data logic goes here
        # For demonstration, we'll just print the response body
        self.log('Page %s cached %s' % (response.url, response.status))
        self.log(response.body)

    def handle_error(self, failure):
        """
        Handle errors during requests.
        """
        self.log('Request %s failed: %s' % (failure.request.url, failure.check_request.status))


# To run this spider, use the command: scrapy crawl cache_spider