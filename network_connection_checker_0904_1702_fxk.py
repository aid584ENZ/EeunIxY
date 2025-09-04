# 代码生成时间: 2025-09-04 17:02:53
import scrapy
import requests
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from urllib3.exceptions import MaxRetryError
import logging


# 设置日志配置
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)


class NetworkConnectionChecker(scrapy.Spider):
    name = "network_connection_checker"
    allowed_domains = []
    start_urls = []

    def __init__(self, *args, **kwargs):
        # 从kwargs中获取要检查的URL
        self.target_url = kwargs.get('target_url', None)
        if not self.target_url:
            raise NotConfigured("Missing target URL")
        self.start_urls = [self.target_url]
        super(NetworkConnectionChecker, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 如果响应状态码为200，则认为网络连接成功
        if response.status == 200:
            logging.info(f"Connection to {self.target_url} is successful.")
        else:
            logging.error(f"Failed to connect to {self.target_url}. Status code: {response.status}")

    def start_requests(self):
        # 生成网络请求并捕获异常
        try:
            yield scrapy.Request(url=self.target_url, callback=self.parse)
        except MaxRetryError as e:
            logging.error(f"Connection failed due to maximum retries reached: {e}")
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Connection failed due to a connection error: {e}")


# 程序入口
def main():
    process = CrawlerProcess()
    process.crawl(NetworkConnectionChecker, target_url="https://www.example.com")
    process.start()


if __name__ == "__main__":
    main()