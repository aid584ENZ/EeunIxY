# 代码生成时间: 2025-08-09 02:17:04
import scrapy


# 表单数据验证器
class FormValidator:
    """
    用于验证表单数据的类，确保数据符合预期的格式和规则。
    """

    def __init__(self, rules):
        """
        初始化验证器，传入验证规则。
        :param rules: 字典，包含字段名和对应的验证规则函数。
        """
        self.rules = rules

    def validate(self, data):
        """
        验证表单数据。
        :param data: 字典，包含待验证的表单数据。
        :return: 验证结果，包括成功与否的标志和错误信息。
        """
        errors = {}
        for field, rule in self.rules.items():
            if field not in data:
                errors[field] = f"{field} is required"
                continue

            try:
                if not rule(data[field]):
                    errors[field] = f"Validation failed for {field}"
            except Exception as e:
                errors[field] = str(e)

        if errors:
            return {'success': False, 'errors': errors}
        else:
            return {'success': True, 'errors': None}


# 示例使用
if __name__ == '__main__':
    # 定义验证规则
    rules = {
        'username': lambda x: x.isalpha() and 3 <= len(x) <= 15,
        'email': lambda x: '@' in x and '.' in x,
        'age': lambda x: isinstance(x, int) and 0 < x < 100
    }

    # 创建验证器实例
    validator = FormValidator(rules)

    # 待验证数据
    data_to_validate = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'age': 30
    }

    # 执行验证
    result = validator.validate(data_to_validate)

    # 打印结果
    print(result)