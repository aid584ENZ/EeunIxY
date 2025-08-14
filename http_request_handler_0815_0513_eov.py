# 代码生成时间: 2025-08-15 05:13:58
import scrapy
from scrapy.http import Request
from scrapy.exceptions import NotConfigured

"""
HTTP请求处理器
该模块提供了一个简单的HTTP请求处理器，用于发送HTTP请求并处理响应。
"""

class HttpRequestHandler:
    """HTTP请求处理器类"""
    def __init__(self, timeout=10, user_agent=None):
        """初始化HTTP请求处理器"""
        self.timeout = timeout
        self.user_agent = user_agent
        self.client = scrapy.crawler.CrawlerProcess()

    def send_request(self, url, method='GET', headers=None, data=None, cookies=None, callback=None):
        """发送HTTP请求并处理响应
        
        参数:
            url (str): 请求的URL
            method (str): 请求方法（GET或POST，默认GET）
            headers (dict): 请求头
            data (dict): POST请求的数据
            cookies (dict): Cookies
            callback (callable): 回调函数，用于处理响应
        
        返回:
            response (scrapy.Response): 响应对象
        """
        if not url:
            raise ValueError("URL不能为空")
        
        if method not in ['GET', 'POST']:
            raise ValueError("请求方法必须是GET或POST")
        
        # 设置请求头
        if headers is None:
            headers = {}
        
        if self.user_agent:
            headers['User-Agent'] = self.user_agent
        
        # 设置Cookies
        if cookies is None:
            cookies = {}
        
        # 创建请求
        request = Request(
            url=url,
            method=method,
            headers=headers,
            body=data,
            cookies=cookies,
            callback=callback,
            timeout=self.timeout
        )
        
        # 发送请求
        try:
            response = self.client.crawl(request)
        except Exception as e:
            raise NotConfigured(f"请求失败: {str(e)}")
        
        return response

    def get(self, url, callback=None, **kwargs):
        """发送GET请求"""
        return self.send_request(url, 'GET', callback=callback, **kwargs)

    def post(self, url, data=None, callback=None, **kwargs):
        """发送POST请求"""
        return self.send_request(url, 'POST', data=data, callback=callback, **kwargs)

# 示例用法
if __name__ == '__main__':
    handler = HttpRequestHandler()
    url = 'https://example.com'
    response = handler.get(url)
    print(response.status)
    print(response.body)
