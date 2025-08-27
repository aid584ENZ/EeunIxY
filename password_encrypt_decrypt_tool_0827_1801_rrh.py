# 代码生成时间: 2025-08-27 18:01:16
import hashlib
import base64

class PasswordManager:
    """
    A utility class to encrypt and decrypt passwords.
    It uses SHA-256 for hashing and base64 for encoding.
    """

    def __init__(self, salt=None):
        # Use a default salt if none is provided
        self.salt = salt if salt else 'default_salt'

    def encrypt_password(self, password):
        """
        Encrypts a password using SHA-256 hashing and base64 encoding.

        Args:
            password (str): The password to be encrypted.

        Returns:
            str: The encrypted password.
        """
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")

        # Combine password with salt and hash it using SHA-256
        password_with_salt = password + self.salt
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

        # Encode the hash in base64
        encrypted_password = base64.b64encode(hashed_password.encode()).decode()

        return encrypted_password

    def decrypt_password(self, encrypted_password):
        """
        Decrypts a password by reversing the encryption process.

        Args:
            encrypted_password (str): The encrypted password to be decrypted.

        Returns:
            str: The decrypted password hash.
        """
        if not isinstance(encrypted_password, str):
            raise ValueError("Encrypted password must be a string.")

        # Decode the base64 encoded password
        try:
            hash_bytes = base64.b64decode(encrypted_password)
            hashed_password = hash_bytes.decode()

            # Since we can't reverse SHA-256, we return the hash
            return hashed_password
        except Exception as e:
            # Handle errors during decryption
            raise ValueError("Failed to decrypt password: " + str(e))

    def verify_password(self, password, encrypted_password):
        """
        Verifies a password against its encrypted version.

        Args:
            password (str): The password to verify.
            encrypted_password (str): The encrypted password to compare against.

        Returns:
            bool: True if they match, False otherwise.
        """
        new_encrypted_password = self.encrypt_password(password)
        return new_encrypted_password == encrypted_password

# Example usage
if __name__ == '__main__':
    password_manager = PasswordManager()
    original_password = 'mysecretpassword123'
    encrypted = password_manager.encrypt_password(original_password)
    print('Encrypted:', encrypted)
    decrypted = password_manager.decrypt_password(encrypted)
    print('Decrypted:', decrypted)
    is_verified = password_manager.verify_password(original_password, encrypted)
    print('Verification:', is_verified)