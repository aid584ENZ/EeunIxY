# 代码生成时间: 2025-09-04 00:45:47
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import schedule
import time
from twisted.internet import reactor
from scrapy.exceptions import NotConfigured

"""
A Scrapy project that includes a scheduled job spider.
This spider can be used to run specific Scrapy spiders at specific times.
"""

class ScheduledJobSpider(scrapy.Spider):
    name = 'scheduled_job_spider'
    custom_settings = {
        'SCHEDULER': 'scrapy_redis.scheduler.Scheduler',
        'SCHEDULER_PERSIST': True,
        'SCHEDULER_QUEUE_CLASS': 'scrapy_redis.queue.SpiderPriorityQueue',
        'SCHEDULER_SERIALIZER': 'scrapy_redis.pickle',
        'SCHEDULER_FLUSH_ON_START': True,
        'SCHEDULER_JOB_DIR': 'scrapy:jobs',
    }

    def __init__(self, spider_name, interval, *args, **kwargs):
        super(ScheduledJobSpider, self).__init__(*args, **kwargs)
        self.spider_name = spider_name
        self.interval = interval  # Interval in seconds

    def start_requests(self):
        """
        Start a request that will trigger the scheduled job.
        """
        self.logger.info(f'Scheduling {self.spider_name} to run every {self.interval} seconds.')
        schedule.every(self.interval).seconds.do(self.run_spider)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def run_spider(self):
        """
        Trigger the actual spider to run.
        """
        try:
            settings = get_project_settings()
            process = CrawlerProcess(settings)
            process.crawl(self.spider_name)
            process.start()
        except NotConfigured as e:
            self.logger.error(f'Spider {self.spider_name} is not configured: {e}')
        except Exception as e:
            self.logger.error(f'An error occurred while running spider {self.spider_name}: {e}')


def main():
    """
    Main function to configure logging and start the scheduled job spider.
    """
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    spider_name = 'example_spider'  # The name of the spider to schedule
    interval = 60 * 60  # Run the spider every hour (3600 seconds)
    process = CrawlerProcess(get_project_settings())
    process.crawl(ScheduledJobSpider, spider_name=spider_name, interval=interval)
    process.start()

if __name__ == '__main__':
    main()