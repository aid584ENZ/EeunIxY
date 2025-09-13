# 代码生成时间: 2025-09-14 07:36:47
import json
from scrapy.exceptions import NotConfigured

"""
JSON数据格式转换器，使用Scrapy框架创建。
提供将JSON字符串转换为Python字典的功能，并处理转换过程中可能发生的错误。
"""

class JsonDataConverter:
    def __init__(self):
        """
        初始化转换器。
        """
        pass

    def convert_to_dict(self, json_string):
        """
        将JSON字符串转换为Python字典。

        参数:
        json_string -- 要转换的JSON字符串。

        返回:
        dict -- 转换后的Python字典。

        抛出:
        json.JSONDecodeError -- 如果JSON字符串格式不正确。
        """
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise NotConfigured(f"JSON解析错误：{e}")

    def convert_to_json(self, data, ensure_ascii=False, **kwargs):
        """
        将Python字典转换为JSON字符串。

        参数:
        data -- 要转换的Python字典。
        ensure_ascii -- 是否确保输出的JSON字符串只包含ASCII字符。
        **kwargs -- 传递给json.dumps的其他参数。

        返回:
        str -- 转换后的JSON字符串。

        """
        return json.dumps(data, ensure_ascii=ensure_ascii, **kwargs)

# 使用示例
if __name__ == "__main__":
    converter = JsonDataConverter()
    json_str = "{"name": "John", "age": 30}"
    try:
        data = converter.convert_to_dict(json_str)
        json_str_converted = converter.convert_to_json(data, ensure_ascii=True)
        print(f"转换后的JSON字符串：{json_str_converted}")
    except NotConfigured as e:
        print(f"错误：{e}")