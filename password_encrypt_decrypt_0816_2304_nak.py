# 代码生成时间: 2025-08-16 23:04:57
import hashlib
import base64
from scrapy.utils.python import to_bytes, to_unicode

"""
A simple password encrypt and decrypt utility using Python and Scrapy's utility functions.
This tool uses SHA-256 for hashing and base64 for encoding the hashed password.
"""


class PasswordUtility:
    def __init__(self, password):
        """Initialize the PasswordUtility with a password."""
        self.password = to_bytes(password)

    def encrypt(self):
        """Encrypt the password using SHA-256 and base64."""
        try:
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(self.password).digest()
            # Encode the hashed password using base64
            encrypted_password = base64.b64encode(hashed_password)
            return to_unicode(encrypted_password)
        except Exception as e:
            # Handle any exceptions that occur during encryption
            print(f"An error occurred during encryption: {e}")
            return None

    def decrypt(self, encrypted_password):
        """Decrypt the password from base64 encoded SHA-256 hash."""
        try:
            # Decode the encrypted password from base64
            decoded_password = base64.b64decode(encrypted_password)
            # Since we hashed the password, we can't truly 'decrypt' it,
            # but we can verify if the provided encrypted password matches the original hash
            original_hash = hashlib.sha256(self.password).digest()
            if decoded_password == original_hash:
                return True
            else:
                return False
        except Exception as e:
            # Handle any exceptions that occur during decryption
            print(f"An error occurred during decryption: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    password = "mysecretpassword"
    utility = PasswordUtility(password)
    encrypted = utility.encrypt()
    print(f"Encrypted password: {encrypted}")
    decrypted = utility.decrypt(encrypted)
    print(f"Password decrypted successfully: {decrypted}")