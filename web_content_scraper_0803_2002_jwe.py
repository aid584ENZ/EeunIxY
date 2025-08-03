# 代码生成时间: 2025-08-03 20:02:27
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Spider


# 定义一个Spider类，继承自scrapy.spiders.Spider
class WebContentScraperSpider(Spider):
    name = 'web_content_scraper'  # 爬虫的名称
    allowed_domains = []  # 允许爬取的域名可以在这里指定
    start_urls = ['http://example.com']  # 爬取开始的URL列表

    def parse(self, response):
        # 解析响应内容
        try:
            # 抓取网页的标题
            title = response.css('title::text').get()
            # 抓取网页中所有的段落
            paragraphs = response.css('p::text').getall()

            # 将抓取到的数据打印出来
            yield {
                'title': title,
                'paragraphs': paragraphs
            }
        except Exception as e:
            # 错误处理
            print(f"An error occurred: {e}")
            raise CloseSpider('Error parsing the page')


# 设置Scrapy爬虫运行参数
process = CrawlerProcess(settings={
    'FEEDS': {
        'items.json': {
            'format': 'json',
            'encoding': 'utf-8',
            'store_empty': False,
        },
    },
    'FEED_EXPORTERS': {'json': 'scrapy.exporters.JsonItemExporter'},
    'LOG_LEVEL': 'INFO'
})

# 启动爬虫
process.crawl(WebContentScraperSpider)
process.start()
