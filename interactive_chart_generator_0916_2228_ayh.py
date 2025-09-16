# 代码生成时间: 2025-09-16 22:28:43
import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.exceptions import CloseSpider
from scrapy.utils.project import get_project_settings
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.layouts import column


# 交互式图表生成器
class InteractiveChartGenerator:
    def __init__(self):
        # 初始化Scrapy设置
        self.settings = get_project_settings()
        self.process = CrawlerProcess(self.settings)

    def run_spider(self, spider_cls, *args, **kwargs):
        """
        运行Scrapy爬虫
        :param spider_cls: 爬虫类
        :param args: 爬虫参数
        :param kwargs: 爬虫关键字参数
        :return: None
        """
        try:
            self.process.crawl(spider_cls, *args, **kwargs)
            self.process.start()
        except CloseSpider as e:
            print(f"爬虫关闭: {e}")
        except Exception as e:
            print(f"运行爬虫时出错: {e}")

    def generate_chart(self, data):
        """
        生成交互式图表
        :param data: 图表数据
        :return: None
        """
        try:
            # 创建数据源
            source = ColumnDataSource(data)

            # 创建图表
            p = figure(title="交互式图表", x_axis_label='X轴', y_axis_label='Y轴')
            p.line(x='x', y='y', source=source)

            # 输出图表到HTML文件
            output_file("chart.html")
            show(column(p))
        except Exception as e:
            print(f"生成图表时出错: {e}")

# 示例爬虫
class ExampleSpider(Spider):
    name = "example"
    start_urls = ["http://example.com"]

    def parse(self, response):
        # 示例解析函数
        data = {
            'x': [1, 2, 3, 4, 5],
            'y': [2, 5, 8, 2, 7]
        }
        yield data


# 主函数
def main():
    # 创建交互式图表生成器实例
    chart_generator = InteractiveChartGenerator()

    # 运行爬虫
    chart_generator.run_spider(ExampleSpider)

    # 获取爬虫结果
    # 注意：这里假设爬虫结果存储在名为"example"的Spider中
    # 在实际应用中，需要根据实际情况修改这部分代码
    spider_data = ExampleSpider.data

    # 生成图表
    chart_generator.generate_chart(spider_data)

if __name__ == "__main__":
    main()