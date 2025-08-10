# 代码生成时间: 2025-08-10 23:36:45
import os
import zipfile
import tarfile
from scrapy import Spider, Request

"""
A utility tool to unzip files using Python and Scrapy framework.
"""

class UnzipTool:
    """
    A class to handle the extraction of files from zip and tar archives.
    """

    def __init__(self, archive_path):
        """
        Initialize the UnzipTool with the path to the archive file.
        :param archive_path: The path to the archive file.
        """
        self.archive_path = archive_path

    def extract(self, output_path):
        """
        Extract the files from the archive to the specified output path.
        :param output_path: The path to extract the files to.
        """
        try:
            if self.archive_path.endswith('.zip'):
                self._extract_zip(output_path)
            elif self.archive_path.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2')):
                self._extract_tar(output_path)
            else:
                raise ValueError(f"Unsupported archive format: {self.archive_path}")
        except Exception as e:
            print(f"An error occurred while extracting the archive: {e}")

    def _extract_zip(self, output_path):
        """
        Extract a zip archive to the specified output path.
        :param output_path: The path to extract the zip archive to.
        """
        with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
            print(f"Extracted zip archive to {output_path}")

    def _extract_tar(self, output_path):
        """
        Extract a tar archive to the specified output path.
        :param output_path: The path to extract the tar archive to.
        """
        with tarfile.open(self.archive_path, 'r') as tar_ref:
            tar_ref.extractall(output_path)
            print(f"Extracted tar archive to {output_path}")

# Example usage:
if __name__ == '__main__':
    archive_path = 'path_to_your_archive_file'
    output_path = 'path_to_extract_files_to'
    unzip_tool = UnzipTool(archive_path)
    unzip_tool.extract(output_path)