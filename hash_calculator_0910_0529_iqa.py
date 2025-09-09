# 代码生成时间: 2025-09-10 05:29:18
import hashlib


# 主类 HashCalculator, 用于计算字符串的哈希值
class HashCalculator:
    """
    哈希值计算工具，支持多种哈希算法。
    """

    def __init__(self):
        """
        初始化 HashCalculator 实例。
        """
        pass

    def calculate_hash(self, algorithm, data):
        """
        计算给定数据的哈希值。

        :param algorithm: 哈希算法名称，如 'md5', 'sha1', 'sha256' 等。
        :param data: 需要计算哈希值的原始数据。
        :return: 计算得到的哈希值。
        :raises ValueError: 当算法不支持或数据为空时。
        """
        if not data:
            raise ValueError("数据不能为空。")"

        try:
            return getattr(hashlib, algorithm)(data.encode()).hexdigest()
        except AttributeError:
            raise ValueError(f"不支持的哈希算法: {algorithm}")

    def calculate_md5(self, data):
        """
        计算 MD5 哈希值的快捷方法。

        :param data: 需要计算哈希值的原始数据。
        :return: MD5 哈希值。
        """
        return self.calculate_hash('md5', data)

    def calculate_sha1(self, data):
        """
        计算 SHA1 哈希值的快捷方法。

        :param data: 需要计算哈希值的原始数据。
        :return: SHA1 哈希值。
        """
        return self.calculate_hash('sha1', data)

    def calculate_sha256(self, data):
        """
        计算 SHA256 哈希值的快捷方法。

        :param data: 需要计算哈希值的原始数据。
        :return: SHA256 哈希值。
        """
        return self.calculate_hash('sha256', data)


# 示例用法
if __name__ == '__main__':
    # 创建 HashCalculator 实例
    calculator = HashCalculator()

    # 计算数据的 MD5 哈希值
    data = 'Hello, World!'
    md5_hash = calculator.calculate_md5(data)
    print(f'MD5 Hash: {md5_hash}')
    
    # 计算数据的 SHA1 哈希值
    sha1_hash = calculator.calculate_sha1(data)
    print(f'SHA1 Hash: {sha1_hash}')
    
    # 计算数据的 SHA256 哈希值
    sha256_hash = calculator.calculate_sha256(data)
    print(f'SHA256 Hash: {sha256_hash}')