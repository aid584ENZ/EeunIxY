# 代码生成时间: 2025-08-20 19:47:50
import os
import re
from scrapy.exceptions import DropItem

"""
批量文件重命名工具
"""

class BulkFileRenamer:
    def __init__(self, directory):
        """
        初始化重命名工具
        :param directory: 需要重命名文件的目录
        """
        self.directory = directory

    def rename_files(self, pattern, replacement):
        """
        批量重命名文件
        :param pattern: 正则表达式模式，用于匹配文件名中需要替换的部分
        :param replacement: 用于替换匹配结果的字符串
        """
        for filename in os.listdir(self.directory):
            try:
                new_filename = re.sub(pattern, replacement, filename)
                if new_filename != filename:
                    old_path = os.path.join(self.directory, filename)
                    new_path = os.path.join(self.directory, new_filename)
                    os.rename(old_path, new_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming file '{filename}': {e}")
            except re.error as e:
                print(f"Regex error in '{filename}': {e}")

    def rename_files_with_date(self, date_format):
        """
        使用日期格式重命名文件
        :param date_format: 日期格式字符串，例如 '%Y-%m-%d'
        """
        current_date = datetime.datetime.now().strftime(date_format)
        for filename in os.listdir(self.directory):
            try:
                new_filename = f"{current_date}_{filename}"
                old_path = os.path.join(self.directory, filename)
                new_path = os.path.join(self.directory, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming file '{filename}': {e}")

# 使用示例
if __name__ == '__main__':
    directory = "/path/to/your/directory"
    renamer = BulkFileRenamer(directory)
    # 重命名文件，将文件名中的 'old' 替换为 'new'
    renamer.rename_files(r"old", "new")
    # 使用日期格式重命名文件
    renamer.rename_files_with_date("%Y%m%d")
