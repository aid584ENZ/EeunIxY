# 代码生成时间: 2025-07-31 11:47:02
import scrapy

"""
数学计算工具集
提供基础的数学运算功能，包括加、减、乘、除等
"""


class MathCalculator:
    """
    数学计算器类，包含加、减、乘、除等方法
    """

    def add(self, a, b):
        """
        加法运算
        :param a: 第一个数字
        :param b: 第二个数字
        :return: 两个数字相加的结果
        """
        try:
            return a + b
        except TypeError:
            raise ValueError("两个操作数必须是数字类型")

    def subtract(self, a, b):
        """
        减法运算
        :param a: 第一个数字
        :param b: 第二个数字
        :return: 两个数字相减的结果
        """
        try:
            return a - b
        except TypeError:
            raise ValueError("两个操作数必须是数字类型")

    def multiply(self, a, b):
        """
        乘法运算
        :param a: 第一个数字
        :param b: 第二个数字
        :return: 两个数字相乘的结果
        """
        try:
            return a * b
        except TypeError:
            raise ValueError("两个操作数必须是数字类型")

    def divide(self, a, b):
        """
        除法运算
        :param a: 第一个数字
        :param b: 第二个数字
        :return: 两个数字相除的结果
        """
        try:
            if b == 0:
                raise ZeroDivisionError("除数不能为0")
            return a / b
        except TypeError:
            raise ValueError("两个操作数必须是数字类型")
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)


# 示例用法
if __name__ == "__main__":
    calculator = MathCalculator()
    print("5 + 3 =", calculator.add(5, 3))
    print("5 - 3 =", calculator.subtract(5, 3))
    print("5 * 3 =", calculator.multiply(5, 3))
    print("5 / 3 =", calculator.divide(5, 3))
