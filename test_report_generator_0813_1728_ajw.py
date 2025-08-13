# 代码生成时间: 2025-08-13 17:28:01
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem
from scrapy.loader import ItemLoader
from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.utils.project import get_project_settings
import csv
import json
import logging

# 定义Item
class TestReportItem(Item):
    url = Field()
    status_code = Field()
    success = Field()
    message = Field()

# 测试报告生成器Spider
class TestReportGeneratorSpider(Spider):
    name = 'test_report_generator'
    allowed_domains = []
    start_urls = []

    def __init__(self, test_urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_urls = test_urls if test_urls else []

    def start_requests(self):
        for url in self.test_urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.error_callback)

    def parse(self, response):
        item_loader = ItemLoader(item=TestReportItem(), response=response)
        item_loader.add_value('url', response.url)
        item_loader.add_value('status_code', response.status)
        item_loader.add_value('success', response.status in range(200, 299))
        item_loader.add_value('message', 'Success' if response.status in range(200, 299) else 'Error')
        yield item_loader.load_item()

    def error_callback(self, failure):
        self.logger.error(f'Error processing {failure.request.url} - {failure.getErrorMessage()}')
        raise DropItem(f'Error processing {failure.request.url}')

# 测试报告生成器Pipeline
class TestReportGeneratorPipeline:
    def open_spider(self, spider):
        self.file = open('test_report.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['URL', 'Status Code', 'Success', 'Message'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([item['url'], item['status_code'], item['success'], item['message']])
        return item

# 设置
def settings():
    return {
        'ITEM_PIPELINES': {'test_report_generator.TestReportGeneratorPipeline': 300},
        'USER_AGENT': 'TestReportGenerator/1.0',
        'LOG_LEVEL': logging.INFO,
    }

# 主函数
def main():
    # 创建CrawlerProcess实例
    process = CrawlerProcess(settings=get_project_settings())
    # 添加Spider
    process.crawl(TestReportGeneratorSpider, test_urls=['https://example.com'])
    # 启动爬虫
    process.start()

if __name__ == '__main__':
    main()