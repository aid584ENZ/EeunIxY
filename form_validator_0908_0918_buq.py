# 代码生成时间: 2025-09-08 09:18:45
import scrapy
from scrapy.exceptions import DropItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from scrapy.item import Field
from scrapy.utils.misc import arg_to_iter
from w3lib.html import remove_tags
from scrapy.utils.python import to_bytes, to_unicode

# 定义一个Item，用于存储表单数据的结构
class FormItem(scrapy.Item):
    name = Field()  # 姓名
    age = Field()  # 年龄
    email = Field()  # 邮箱

# 定义一个表单数据验证器
class FormValidator:
    def __init__(self) -> None:
        # 初始化验证器
        pass

    def validate_name(self, name: str) -> bool:
        """
        验证姓名是否有效

        :param name: 姓名
        :return: 布尔值，True表示有效，False表示无效
        """
        if not name:
            return False
        if not name.isalpha():
            return False
        return True

    def validate_age(self, age: str) -> bool:
        """
        验证年龄是否有效

        :param age: 年龄
        :return: 布尔值，True表示有效，False表示无效
        """
        try:
            age = int(age)
            if age < 0 or age > 100:
                return False
            return True
        except ValueError:
            return False

    def validate_email(self, email: str) -> bool:
        """
        验证邮箱是否有效

        :param email: 邮箱
        :return: 布尔值，True表示有效，False表示无效
        """
        if not email:
            return False
        if '@' not in email:
            return False
        if '.' not in email.split('@')[1]:
            return False
        return True

    def validate_item(self, item: FormItem) -> bool:
        """
        验证Item是否有效

        :param item: 表单数据Item
        :return: 布尔值，True表示有效，False表示无效
        """
        if not self.validate_name(item['name']):
            return False
        if not self.validate_age(item['age']):
            return False
        if not self.validate_email(item['email']):
            return False
        return True

# 定义一个Spider，使用表单数据验证器
class FormSpider(scrapy.Spider):
    name = 'form_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/form']

    def parse(self, response):
        """
        解析表单数据并验证

        :param response: 响应对象
        :return: None
        """
        # 解析表单数据
        name = response.xpath('//input[@name="name"]/@value').extract_first()
        age = response.xpath('//input[@name="age"]/@value').extract_first()
        email = response.xpath('//input[@name="email"]/@value').extract_first()

        # 创建一个ItemLoader，用于加载数据
        item_loader = ItemLoader(item=FormItem(), response=response)
        item_loader.default_input_processor = MapCompose(remove_tags, to_unicode)
        item_loader.add_value('name', name)
        item_loader.add_value('age', age)
        item_loader.add_value('email', email)

        # 加载数据并验证
        item = item_loader.load_item()
        validator = FormValidator()
        if validator.validate_item(item):
            yield item
        else:
            # 如果数据无效，抛出DropItem异常
            raise DropItem(f'Invalid item: {item}')
