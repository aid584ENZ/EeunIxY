# 代码生成时间: 2025-09-17 12:01:45
import os
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
import re

"""
Batch Rename Tool using Python and Scrapy framework.
This program provides a simple way to batch rename files in a directory.

Attributes:
    source_folder (str): The directory path where files are located.
    target_folder (str): The directory path where renamed files will be saved.
    rename_pattern (str): The regex pattern used to match and replace file names.
    rename_format (str): The new format for file names after matching the pattern.

Methods:
    rename_files(): Renames files in the source_folder according to the rename_pattern and saves them in the target_folder.
"""

class BatchRenameTool:
    def __init__(self, source_folder, target_folder, rename_pattern, rename_format):
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.rename_pattern = rename_pattern
        self.rename_format = rename_format

    def rename_files(self):
        # Check if source and target directories exist
        if not os.path.exists(self.source_folder):
            raise FileNotFoundError(f"Source directory not found: {self.source_folder}")
        if not os.path.exists(self.target_folder):
            raise FileNotFoundError(f"Target directory not found: {self.target_folder}")

        # Iterate through files in the source directory
        for filename in os.listdir(self.source_folder):
            try:
                # Create a full path for the file
                file_path = os.path.join(self.source_folder, filename)

                # Check if the file matches the rename pattern
                match = re.match(self.rename_pattern, filename)
                if match:
                    # Generate the new filename using the rename format
                    new_filename = re.sub(self.rename_pattern, self.rename_format, filename)
                    new_file_path = os.path.join(self.target_folder, new_filename)

                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} to {new_filename}")
                else:
                    print(f"Skipped {filename}, no match found")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

# Example usage
if __name__ == '__main__':
    source_folder = 'path/to/source/directory'
    target_folder = 'path/to/target/directory'
    rename_pattern = r'^old_pattern_(\d+)\.txt$'  # Example regex pattern
    rename_format = r'new_pattern_\1.txt'  # Example rename format

    rename_tool = BatchRenameTool(source_folder, target_folder, rename_pattern, rename_format)
    rename_tool.rename_files()