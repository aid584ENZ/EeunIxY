# 代码生成时间: 2025-09-22 15:24:14
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, Request
from scrapy.exceptions import CloseSpider
import re
import collections
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)

class TextFileAnalyzer(Spider):
    '''
    文本文件内容分析器
    分析文本文件中的内容，如统计词频等
    '''
    name = 'text_file_analyzer'
    allowed_domains = []  # 由于这是一个文本分析器，不需要设置域名
    start_urls = []  # 初始URL列表，这里为空，因为需要从文件读取内容

    def __init__(self, file_path, *args, **kwargs):
        super(TextFileAnalyzer, self).__init__(*args, **kwargs)
        self.file_path = file_path  # 文本文件路径

    def parse(self, response):
        # 由于这是一个文本分析器，不需要解析response，直接处理文件内容
        self.process_file(self.file_path)

    def process_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.analyze_content(content)
        except FileNotFoundError:
            logging.error(f'文件 {file_path} 未找到。')
            raise CloseSpider(reason='文件未找到')
        except Exception as e:
            logging.error(f'处理文件时发生错误：{e}')
            raise CloseSpider(reason='处理文件时发生错误')

    def analyze_content(self, content):
        '''
        分析文件内容，统计词频
        '''
        # 使用正则表达式去掉标点符号和数字
        content = re.sub(r'[\d\W]+', ' ', content)
        # 分词
        words = content.split()
        # 统计词频
        word_count = collections.Counter(words)
        # 输出词频统计结果
        logging.info(f'词频统计结果：{word_count}')

# 运行分析器
def run_analyzer(file_path):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    })
    process.crawl(TextFileAnalyzer, file_path=file_path)
    process.start()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('使用方法：python text_file_analyzer.py 文件路径')
    else:
        run_analyzer(sys.argv[1])