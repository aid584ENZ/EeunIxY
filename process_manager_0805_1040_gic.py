# 代码生成时间: 2025-08-05 10:40:44
import logging
import psutil
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging


# 配置日志
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# 增强安全性

"""
# 改进用户体验
进程管理器
"""
class ProcessManager:
    def __init__(self, settings_path='settings.py'):
        self.settings_path = settings_path
        self.processes = {}
        self.settings = get_project_settings(self.settings_path)
        self.crawler_process = CrawlerProcess(self.settings)

    """
    启动Scrapy爬虫进程
    """
    def start_spider(self, spider_name):
        try:
            self.crawler_process.crawl(spider_name)
            self.crawler_process.start()
        except Exception as e:
            logger.error(f"Failed to start spider {spider_name}: {str(e)}")

    """
    终止Scrapy爬虫进程
    """
# TODO: 优化性能
    def stop_spider(self, spider_name):
# TODO: 优化性能
        try:
            for process in self.crawler_process.crawlers:
# 增强安全性
                if process.spider.name == spider_name:
# TODO: 优化性能
                    process.stop()
        except Exception as e:
            logger.error(f"Failed to stop spider {spider_name}: {str(e)}")

    """
    终止所有Scrapy爬虫进程
    """
    def stop_all_spiders(self):
# 增强安全性
        try:
            for process in self.crawler_process.crawlers:
                process.stop()
        except Exception as e:
            logger.error("Failed to stop all spiders: {0}".format(str(e)))

    """
# TODO: 优化性能
    获取当前运行的所有进程信息
    """
# 增强安全性
    def get_process_info(self):
        try:
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                yield proc.info
# 添加错误处理
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logger.error("Failed to retrieve process info")

"""
主程序入口
"""
if __name__ == '__main__':
    process_manager = ProcessManager()

    # 示例：启动爬虫
    process_manager.start_spider('example_spider')

    # 示例：终止爬虫
    # process_manager.stop_spider('example_spider')

    # 示例：终止所有爬虫
    # process_manager.stop_all_spiders()

    # 示例：获取进程信息
    # process_info = list(process_manager.get_process_info())
    # for info in process_info:
# NOTE: 重要实现细节
    #     print(info)