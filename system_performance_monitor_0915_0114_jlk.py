# 代码生成时间: 2025-09-15 01:14:09
import scrapy
def get_system_info():
    """
    获取系统基本信息
    """
    import psutil
    system_info = {}
    system_info['cpu_usage'] = psutil.cpu_percent(interval=1)
    system_info['memory_usage'] = psutil.virtual_memory().percent
    system_info['disk_usage'] = psutil.disk_usage('/').percent
    return system_info


class SystemPerformanceMonitor(scrapy.Spider):
    name = 'system_performance_monitor'
    allowed_domains = []
    start_urls = []

    def parse(self, response):
        """
        爬虫解析函数
        """
        try:
            system_info = get_system_info()
            print('System Performance Information:')
            for key, value in system_info.items():
                print(f'{key}: {value}%')
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={"USER_AGENT" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                                                "FEED_FORMAT" : "json",
                                                "FEED_URI" : "output.json"})
    process.crawl(SystemPerformanceMonitor)
    process.start()