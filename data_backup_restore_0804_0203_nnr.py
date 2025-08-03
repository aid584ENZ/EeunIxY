# 代码生成时间: 2025-08-04 02:03:54
import os
import shutil
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings

"""
A Scrapy spider for data backup and restore.
This module provides functionalities to backup and restore data.
"""

class DataBackupRestore:

    @staticmethod
    def __init__(self):
        # Load project settings
        settings = get_project_settings()
        self.backup_directory = settings.get('BACKUP_DIRECTORY', 'backup')
        self.data_directory = settings.get('DATA_DIRECTORY', 'data')

    def backup_data(self):
        """Backup data from the data directory to the backup directory."""
        try:
            if not os.path.exists(self.backup_directory):
                os.makedirs(self.backup_directory)

            # Get all files in the data directory
            files = [f for f in os.listdir(self.data_directory) if os.path.isfile(os.path.join(self.data_directory, f))]
            for file in files:
                # Construct full file path
                file_path = os.path.join(self.data_directory, file)
                backup_file_path = os.path.join(self.backup_directory, file)
                # Copy the file to the backup directory
                shutil.copy(file_path, backup_file_path)
            print(f"Data backed up successfully to {self.backup_directory}")
        except Exception as e:
            print(f"Error occurred during backup: {e}")

    def restore_data(self, file_name):
        """Restore data from the backup directory to the data directory."""
        try:
            # Construct full file paths
            backup_file_path = os.path.join(self.backup_directory, file_name)
            data_file_path = os.path.join(self.data_directory, file_name)
            # Check if the file exists in the backup directory
            if not os.path.exists(backup_file_path):
                raise FileNotFoundError(f"File {file_name} not found in backup directory")
            # Copy the file from the backup directory to the data directory
            shutil.copy(backup_file_path, data_file_path)
            print(f"Data restored successfully from {backup_file_path} to {data_file_path}")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Error occurred during restore: {e}")

    def delete_backup(self, file_name):
        """Delete a backup file from the backup directory."""
        try:
            # Construct full file path
            backup_file_path = os.path.join(self.backup_directory, file_name)
            # Check if the file exists in the backup directory
            if os.path.exists(backup_file_path):
                os.remove(backup_file_path)
                print(f"Backup file {file_name} deleted successfully")
            else:
                print(f"File {file_name} not found in backup directory")
        except Exception as e:
            print(f"Error occurred during delete: {e}")

# Example usage:
if __name__ == '__main__':
    backup_restore = DataBackupRestore()
    backup_restore.backup_data()  # Backup data
    backup_restore.restore_data('example_data.txt')  # Restore a specific file
    backup_restore.delete_backup('example_data.txt')  # Delete a backup file