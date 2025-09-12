# 代码生成时间: 2025-09-12 20:32:09
import scrapy
def run_spider(spider_name):
    # 定义Scrapy项目中的spider类
    class MySpider(scrapy.Spider):
        name = spider_name
        custom_settings = {
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        }

        def start_requests(self):
            # 定义初始请求的URL
            url = 'https://example.com'
            yield scrapy.Request(url=url, callback=self.parse, meta={'cookie': 'session=1234567890'})

        def parse(self, response):
            # 解析响应内容
            self.log('Visited %s' % response.url)
            # 假设我们需要提取页面的标题
            title = response.css('title::text').get()
            if title:
                self.log('Title found: %s' % title)
            else:
                raise ValueError('Title not found in response')

    try:
        # 运行Scrapy Spider
        process = CrawlerProcess(settings={'FEEDS': {'"': "tmp.json"}})
        process.crawl(MySpider)
        process.start()
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    # 调用函数，传入Spider名称
    run_spider('example_spider')