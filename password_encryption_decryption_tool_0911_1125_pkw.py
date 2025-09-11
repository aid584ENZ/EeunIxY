# 代码生成时间: 2025-09-11 11:25:37
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.exceptions import NotConfigured

"""
A password encryption and decryption tool using the Scrapy framework.
This tool provides a basic implementation of password encryption and decryption
using the SHA-256 hashing algorithm.
"""

class PasswordEncryptionDecryptionTool:

    def __init__(self, salt=None):
        """Initialize the tool with an optional salt."""
        self.salt = salt if salt else self.generate_salt()

    def generate_salt(self):
        """Generate a random salt for password hashing."""
        import os
        return os.urandom(16).hex()

    def hash_password(self, password):
        """Hash a password using SHA-256 and the salt."""
        try:
            # Convert the password and salt to bytes
            password_bytes = to_bytes(password)
            salt_bytes = to_bytes(self.salt)

            # Concatenate the password and salt
            raw_password = password_bytes + salt_bytes

            # Create a SHA-256 hash object
            hash_object = hashlib.sha256()

            # Update the hash object with the raw password
            hash_object.update(raw_password)

            # Return the hexadecimal hash
            return hash_object.hexdigest()
        except Exception as e:
            # Handle any exceptions during hashing
            raise NotConfigured(f"Error hashing password: {e}")

    def verify_password(self, password, stored_hash):
        """Verify a password against a stored hash."""
        try:
            # Hash the provided password
            hashed_password = self.hash_password(password)

            # Compare the hashed password with the stored hash
            return hashed_password == stored_hash
        except Exception as e:
            # Handle any exceptions during verification
            raise NotConfigured(f"Error verifying password: {e}")

# Example usage
if __name__ == "__main__":
    tool = PasswordEncryptionDecryptionTool()

    # Hash a password
    password = "mysecretpassword"
    hashed_password = tool.hash_password(password)
    print(f"Hashed password: {hashed_password}")

    # Verify the password
    is_valid = tool.verify_password(password, hashed_password)
    print(f"Password is valid: {is_valid}")
