# 代码生成时间: 2025-09-08 16:35:24
# order_processing_spider.py
# 订单处理Scrapy Spider程序

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join
from scrapy.item import Field, Item
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import CloseSpider
from scrapy.exceptions import DropItem
from scrapy.exceptions import NotConfigured
import logging
import json
import os

# 定义订单项目
class OrderItem(Item):
    order_id = Field(output_process=lambda x: x[0:10] if len(x) > 10 else x)  # 订单ID
    customer_name = Field(output_processor=TakeFirst())  # 客户姓名
    order_date = Field(output_processor=TakeFirst())  # 订单日期
    details = Field(output_processor=TakeFirst())  # 订单详情
    status = Field()  # 订单状态
    total_amount = Field()  # 总金额

# 订单处理器
class OrderProcessingSpider(scrapy.Spider):
    name = "order_processing"
    allowed_domains = []  # 允许爬取的域名
    start_urls = []  # 初始URL列表
    custom_settings = {
        'IMAGES_STORE': '/path/to/image/store',  # 图片存储路径
    }

    def __init__(self, *args, **kwargs):
        super(OrderProcessingSpider, self).__init__(*args, **kwargs)
        self.log = logging.getLogger(__name__)
        self.item_loader = ItemLoader(item=OrderItem(), default_output_processor=TakeFirst())
        self.pipelines = []  # 管道列表

    def start_requests(self):
        # 发送初始请求
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析响应
        try:
            data = json.loads(response.body)
            for order in data.get('orders', []):
                self.item_loader.add_value('order_id', order.get('id'))
                self.item_loader.add_value('customer_name', order.get('customer_name'))
                self.item_loader.add_value('order_date', order.get('date'))
                self.item_loader.add_value('details', order.get('details'))
                self.item_loader.add_value('status', order.get('status'))
                self.item_loader.add_value('total_amount', order.get('total_amount'))

                item = self.item_loader.load_item()
                yield item
        except Exception as e:
            self.log.error(f"解析错误：{e}")
            raise CloseSpider(f"解析错误：{e}")

    def process_item(self, item, spider):
        # 处理订单
        try:
            if item.get('status') == 'pending':
                # 处理待处理订单
                self.log.info(f"处理订单：{item['order_id']}")
                # 添加业务逻辑
            elif item.get('status') == 'completed':
                # 处理已完成订单
                self.log.info(f"已完成订单：{item['order_id']}")
                # 添加业务逻辑
            else:
                raise DropItem(f"未知订单状态：{item['status']}")
        except Exception as e:
            self.log.error(f"订单处理错误：{e}")
            raise DropItem(f"订单处理错误：{e}")
        return item

# 图片下载管道
class ImagesDownloaderPipeline:
    def __init__(self, settings):
        self.images_store = settings.get('IMAGES_STORE')
        if not self.images_store:
            raise NotConfigured()

    def process_item(self, item, spider):
        image_urls = item.get('image_urls')
        if image_urls:
            return item
        else:
            raise DropItem('没有图片URL')

    def download_images(self, request, info):
        image = ImagesPipeline()
        return image.download_images(request, info)

# 主程序
if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'DEPTH_LIMIT': 4,  # 爬取深度限制
        'FEED_FORMAT': 'json',  # 输出格式
        'FEED_URI': 'output.json',  # 输出文件
    })
    process.crawl(OrderProcessingSpider)
    process.start()