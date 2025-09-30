# 代码生成时间: 2025-09-30 17:45:49
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.http import Request
import json


# API测试工具
class ApiTester(Spider):
    name = "api_tester"
    allowed_domains = []  # 允许的域（可根据需要添加）
    start_urls = []  # 初始URL列表
    
    # 初始化方法
    def __init__(self, *args, **kwargs):
        super(ApiTester, self).__init__(*args, **kwargs)
        self.url = kwargs.get("url")  # 从参数中获取URL
        self.method = kwargs.get("method", "GET").upper()  # 默认为GET请求
        self.headers = kwargs.get("headers", {})  # 默认头部为空字典
        self.data = kwargs.get("data", {})  # 默认数据为空字典
        self.timeout = kwargs.get("timeout", 10)  # 默认超时时间为10秒
        self.start_urls = [self.url]  # 设置初始URL
    
    # 发送请求并处理响应
    def parse(self, response):
        try:
            # 检查响应状态码
            if response.status != 200:
                yield {
                    "url": self.url,
                    "status": response.status,
                    "error": "Failed to retrieve data"
                }
            else:
                # 解析响应内容
                data = json.loads(response.text)
                yield {
                    "url": self.url,
                    "status": response.status,
                    "data": data
                }
        except json.JSONDecodeError:
            yield {
                "url": self.url,
                "status": response.status,
                "error": "Failed to parse JSON data"
            }
        except Exception as e:
            yield {
                "url": self.url,
                "status": response.status,
                "error": str(e)
            }

    # 发送请求
    def start_requests(self):
        yield Request(
            url=self.url,
            method=self.method,
            headers=self.headers,
            body=json.dumps(self.data) if self.data else None,
            timeout=self.timeout,
            callback=self.parse
        )


# 运行API测试工具
def run_api_tester(url, **kwargs):
    # 创建CrawlerProcess实例
    process = CrawlerProcess()
    # 创建并运行爬虫
    process.crawl(ApiTester, url=url, **kwargs)
    process.start()


# 示例用法
if __name__ == "__main__":
    url = "https://api.example.com/data"
    # 运行API测试工具
    run_api_tester(url, method="POST", headers={"Content-Type": "application/json"}, data={"key": "value"})
