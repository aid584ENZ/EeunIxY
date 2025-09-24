# 代码生成时间: 2025-09-24 21:29:28
import scrapy


# 定义一个Scrapy项目中的Item，用于存放抓取的数据
class WebContentItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


# 定义一个Spider，继承自scrapy.Spider
class WebContentScraper(scrapy.Spider):
    name = 'web_content_scraper'  # Spider的名称
    allowed_domains = ['example.com']  # 允许爬取的域名
    start_urls = ['http://www.example.com/']  # 爬取起始的URL列表
    

    def parse(self, response):
        # 解析响应并提取数据
        # 提取网页标题
        title = response.css('title::text').get()
        # 提取网页内容
        content = response.css('body').get()
        # 创建Item实例
        item = WebContentItem()
        item['url'] = response.url
        item['title'] = title
        item['content'] = content
        yield item

        # 跟随页面内的链接
        for next_page in response.css('a::attr(href)').getall():
            next_page_url = response.urljoin(next_page)
            if next_page_url not in self.visited_urls:
                self.visited_urls.add(next_page_url)
                yield scrapy.Request(url=next_page_url, callback=self.parse)

    # 定义一个集合来记录已经访问过的URL
    visited_urls = set()


# 定义一个Pipeline，用于处理Item中的数据
class WebContentPipeline:
    def process_item(self, item, spider):
        # 处理item中的数据，例如保存到数据库
        # 这里仅作示例，实际使用时需要根据需求实现
        return item

# 在settings.py中，根据需要添加以下配置
# ITEM_PIPELINES = {
#     'web_content_scraper.pipelines.WebContentPipeline': 300,
# }
