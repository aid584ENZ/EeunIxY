# 代码生成时间: 2025-08-21 16:28:43
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.python import to_bytes
import json
import sys


# 定义InteractiveChartGenerator类
class InteractiveChartGenerator(scrapy.commands.ScrapyCommand):
    requires_project = True

    def syntax(self):
        return ""

    def short_desc(self):
        return "Interactive chart generator using Scrapy"

    def run(self, args, opts):
        try:
            # 检查参数是否为空
            if not args:
                raise UsageError('This command requires at least one argument, a URL to scrape data from')

            # 创建CrawlerProcess实例
            process = CrawlerProcess(get_project_settings())

            # 创建Spider实例
            spider = InteractiveChartSpider(args[0])

            # 添加Spider到CrawlerProcess
            process.crawl(spider)

            # 启动CrawlerProcess
            process.start()
        except Exception as e:
            self.log('Error: %s', e, level=log.ERROR)
            sys.exit(1)


# 定义InteractiveChartSpider类
class InteractiveChartSpider(scrapy.Spider):
    name = 'interactive_chart_spider'

    def __init__(self, url):
        super(InteractiveChartSpider, self).__init__()
        self.start_urls = [url]

    def parse(self, response):
        # 解析返回的数据
        try:
            data = json.loads(response.body_as_unicode())
            # 假设数据结构为{'labels': ['Label1', 'Label2'], 'data': [10, 20]}
            labels = data['labels']
            values = data['data']

            # 生成图表代码
            chart_code = self.generate_chart_code(labels, values)

            # 保存图表代码到文件
            with open('chart_code.py', 'w') as f:
                f.write(chart_code)

            self.log('Chart code generated successfully')
        except KeyError:
            raise UsageError('Invalid data format. Expected labels and data keys')
        except Exception as e:
            self.log('Error: %s', e, level=log.ERROR)

    def generate_chart_code(self, labels, values):
        # 生成图表代码
        chart_code = """import matplotlib.pyplot as plt

labels = {}
values = {}

plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.xlabel('Labels')
plt.ylabel('Values')
plt.title('Interactive Chart')
plt.show()""".format(labels, values)

        return chart_code


# 定义main函数
def main():
    InteractiveChartGenerator().run()

if __name__ == '__main__':
    main()