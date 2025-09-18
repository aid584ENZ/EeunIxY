# 代码生成时间: 2025-09-19 06:36:43
#!/usr/bin/env python

"""
定时任务调度器
使用Scrapy框架实现定时任务调度器，用于定期执行Scrapy爬虫任务。
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime


# 配置项
class SpiderScheduler:
    def __init__(self, spider_name, schedule_interval):
        """
        初始化定时任务调度器

        :param spider_name: 爬虫名称
        :param schedule_interval: 定时任务的时间间隔，例如 '0 * * * *' 表示每小时执行一次
        """
        self.spider_name = spider_name
        self.schedule_interval = schedule_interval
        self.scheduler = BackgroundScheduler()
        self.setup_crawler()
        self.setup_scheduler()

    def setup_crawler(self):
        """
        设置Scrapy爬虫
        """
        settings = get_project_settings()
        self.process = CrawlerProcess(settings)

    def setup_scheduler(self):
        """
        设置定时任务调度器
        """
        try:
            # 添加定时任务
            self.scheduler.add_job(self.run_spider, trigger=CronTrigger(self.schedule_interval))
            # 启动调度器
            self.scheduler.start()
        except Exception as e:
            print(f"Error setting up scheduler: {e}")

    def run_spider(self):
        """
        运行Scrapy爬虫
        """
        try:
            # 启动爬虫
            self.process.crawl(self.spider_name)
            # 阻塞直到爬虫执行完毕
            self.process.start()
            print(f"Spider {self.spider_name} executed at {datetime.now()}")
        except Exception as e:
            print(f"Error running spider {self.spider_name}: {e}")

    def stop_scheduler(self):
        """
        停止调度器
        """
        self.scheduler.shutdown()


# 主函数
if __name__ == "__main__":
    # 爬虫名称
    spider_name = "example_spider"
    # 定时任务的时间间隔，例如 '0 * * * *' 表示每小时执行一次
    schedule_interval = "0 * * * *"
    
    # 创建定时任务调度器
    scheduler = SpiderScheduler(spider_name, schedule_interval)

    # 运行定时任务调度器
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # 停止调度器
        scheduler.stop_scheduler()
        print("Scheduler stopped")
