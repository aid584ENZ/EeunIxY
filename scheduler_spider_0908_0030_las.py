# 代码生成时间: 2025-09-08 00:30:12
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# 定义定时任务调度器
class SchedulerSpider(scrapy.Spider):
    '''
    定时任务调度器
    使用APScheduler实现定时任务调度
    '''
    name = 'scheduler_spider'

    def start_requests(self):
        # 设置定时任务
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.fetch_data, CronTrigger(hour=0, minute=0))  # 每天凌晨0点执行
        self.scheduler.start()

    def fetch_data(self):
        '''
        模拟数据抓取任务
        '''
        try:
            print('Fetch data at {}'.format(self.get_current_time()))
        except Exception as e:
            print('Error fetching data:', e)

    def get_current_time(self):
        '''
        获取当前时间
        '''
        import datetime
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def closed(self, reason):
        '''
        关闭定时任务调度器
        '''
        self.scheduler.shutdown(wait=False)

# 定义Scrapy爬虫项目设置
def get_project_settings():
    return get_project_settings().set('FEED_FORMAT', 'json')

# 定义Scrapy爬虫项目入口函数
def main():
    '''
    Scrapy爬虫项目入口函数
    '''
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(SchedulerSpider)
    process.start()

    # 启动Twisted reactor
    reactor.run(installSignalHandlers=False)

if __name__ == '__main__':
    main()