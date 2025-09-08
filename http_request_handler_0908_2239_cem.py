# 代码生成时间: 2025-09-08 22:39:54
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.exceptions import NotConfigured

# 定义HTTP请求处理器
class HttpRequestHandler(Spider):
    def __init__(self, url, method='GET', headers=None, *args, **kwargs):
        super(HttpRequestHandler, self).__init__(*args, **kwargs)
        self.url = url
        self.method = method
        self.headers = headers or {}

    def start_requests(self):
        """
        生成初始请求
        """
        yield Request(
            url=self.url,
            method=self.method.upper(),
            headers=self.headers,
            callback=self.parse,
            errback=self.error_handling
        )

    def parse(self, response):
        """
        处理响应
        """
        # 根据需求处理响应内容
        self.log('Status Code: %s', response.status)
        # 假设输出响应内容
        yield {
            'status': response.status,
            'body': response.body.decode('utf-8')
        }

    def error_handling(self, failure):
        """
        错误处理回调
        """
        # 记录错误日志
        self.log('Error: %s', failure)

# 使用CrawlerProcess运行爬虫
def run_spider(url, method='GET', headers=None):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
    })
    process.crawl(HttpRequestHandler, url=url, method=method, headers=headers)
    process.start()

if __name__ == '__main__':
    # 示例运行
    try:
        url = 'http://example.com'
        method = 'GET'
        headers = {'User-Agent': 'Scrapy/1.8'}
        run_spider(url, method, headers)
    except NotConfigured as e:
        print(f'Error: {e}')
