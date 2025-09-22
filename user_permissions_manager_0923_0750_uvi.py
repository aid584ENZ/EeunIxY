# 代码生成时间: 2025-09-23 07:50:12
# user_permissions_manager.py

"""
User Permissions Manager using Scrapy framework.
This module provides a simple example of a user permissions management system.
"""

import scrapy
from scrapy.crawler import CrawlerProcess

class UserPermissionsManager:
    """
    User Permissions Manager class.
    It handles user permissions and provides methods to add, remove, and check permissions.
    """

    def __init__(self):
        """
        Initialize the UserPermissionsManager with an empty permissions dictionary.
        """
        self.permissions = {}

    def add_user(self, username):
        """
        Add a new user to the permissions system.
        """
        if username not in self.permissions:
            self.permissions[username] = set()
        else:
            raise ValueError(f"User {username} already exists.")

    def remove_user(self, username):
        """
        Remove a user from the permissions system.
        """
        if username in self.permissions:
            del self.permissions[username]
        else:
            raise ValueError(f"User {username} does not exist.")

    def add_permission(self, username, permission):
        """
        Add a permission to a user.
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        self.permissions[username].add(permission)

    def remove_permission(self, username, permission):
        """
        Remove a permission from a user.
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        if permission in self.permissions[username]:
            self.permissions[username].remove(permission)
        else:
            raise ValueError(f"Permission {permission} does not exist for user {username}.")

    def check_permission(self, username, permission):
        """
        Check if a user has a specific permission.
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        return permission in self.permissions[username]

    def list_permissions(self, username):
        """
        List all permissions for a user.
        """
        if username not in self.permissions:
            raise ValueError(f"User {username} does not exist.")
        return list(self.permissions[username])

# Example usage
if __name__ == '__main__':
    manager = UserPermissionsManager()
    try:
        manager.add_user('admin')
        manager.add_permission('admin', 'edit')
        manager.add_permission('admin', 'delete')
        print(manager.check_permission('admin', 'edit'))  # Output: True
        print(manager.list_permissions('admin'))  # Output: ['edit', 'delete']
    except ValueError as e:
        print(e)