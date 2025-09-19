# 代码生成时间: 2025-09-19 17:42:22
import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
from twisted.python.failure import Failure


# 配置日志记录器
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class ErrorLogCollector:
    """
    错误日志收集器，用于收集Scrapy爬虫中的异常信息。
# NOTE: 重要实现细节
    """
    def __init__(self, stats):
        """
# 改进用户体验
        初始化错误日志收集器。
        :param stats: Scrapy的stats对象，用于记录和报告爬虫的统计信息。
        """
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        """
        从Scrapy爬虫中创建错误日志收集器实例。
        :param crawler: Scrapy爬虫实例。
        :return: 错误日志收集器实例。
        """
        # 此函数用于从Scrapy爬虫中提取必要的组件并创建扩展实例
        try:
            ext = cls(crawler.stats)
            crawler.signals.connect(ext.item_error, signal=signals.item_error)
            return ext
        except NotConfigured:
            raise NotConfigured("ErrorLogCollector middleware not configured.")

    def item_error(self, failure, item, response, spider):
        """
        处理项目过程中的错误。
        :param failure: 异常信息。
        :param item: 爬取的项目。
        :param response: 响应对象。
        :param spider: 爬虫实例。
        """
        # 记录错误信息
        self._log_error(failure, item, response, spider)

    def _log_error(self, failure, item, response, spider):
        """
        内部函数，用于记录错误信息。
        :param failure: 异常信息。
        :param item: 爬取的项目。
        :param response: 响应对象。
        :param spider: 爬虫实例。
# 增强安全性
        """
        # 获取异常信息
        exc_type, exc_value, exc_traceback = Failure(failure).getException()

        # 构建错误信息
        error_msg = (
# 添加错误处理
            f"Item: {item!r} | {exc_type.__name__}: {exc_value} | Response URL: {response.url} | Spider: {spider.name}"
# NOTE: 重要实现细节
        )

        # 记录错误日志
# NOTE: 重要实现细节
        logger.error(error_msg)


# 设置Scrapy扩展
extension = ErrorLogCollector