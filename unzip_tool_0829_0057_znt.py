# 代码生成时间: 2025-08-29 00:57:12
import zipfile
import os
from scrapy.exceptions import DropItem

"""
A utility to unzip files using Python.

This module allows you to unzip files in a specified directory
and handle any errors that might occur during the process.
"""

class UnzipTool:
    def __init__(self, directory):
        """Initialize the UnzipTool with a directory to search for zip files."""
        self.directory = directory

    def find_zip_files(self):
        """Find all zip files in the specified directory."""
        zip_files = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.zip'):
                    zip_files.append(os.path.join(root, file))
        return zip_files

    def unzip_file(self, zip_path):
        """Unzip a single zip file to the same directory."""
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(zip_path))
            print(f'Successfully unzipped: {zip_path}')
        except zipfile.BadZipFile:
            print(f'Error: {zip_path} is not a zip file or is corrupt.')
        except Exception as e:
            print(f'An error occurred while unzipping {zip_path}: {e}')

    def unzip_all(self):
        """Unzip all zip files in the directory."""
        zip_files = self.find_zip_files()
        for zip_file in zip_files:
            self.unzip_file(zip_file)

# Example usage
if __name__ == '__main__':
    unzipper = UnzipTool('/path/to/your/zip/files')
    unzipper.unzip_all()