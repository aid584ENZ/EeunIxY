# 代码生成时间: 2025-08-13 23:37:27
import hashlib


# 哈希值计算工具类
class HashCalculator:
    """
    A utility class to calculate hash values for given data.
    """

def calculate_hash(self, data: str, algorithm: str = 'sha256') -> str:
        """
        Calculate the hash value of the provided data using the specified algorithm.

        Args:
            data (str): The data to be hashed.
            algorithm (str): The hash algorithm to use (e.g., 'sha256', 'md5'). Defaults to 'sha256'.

        Returns:
            str: The hash value of the data.

        Raises:
            ValueError: If the algorithm is not supported.
        """
        try:
            # Create a new hash object using the specified algorithm
            hash_obj = getattr(hashlib, algorithm)()
            # Update the hash object with the data to be hashed
            hash_obj.update(data.encode())
            # Return the hex digest of the hash
            return hash_obj.hexdigest()
        except AttributeError:
            # Raise a ValueError if the algorithm is not supported
            raise ValueError(f"Unsupported algorithm: {algorithm}
Supported algorithms are: {', '.join(hashlib.algorithms_available_)}}")

def main():
    """
    Main function to demonstrate the usage of the HashCalculator class.
    """
    # Create an instance of the HashCalculator class
    calculator = HashCalculator()

    # Example data to be hashed
    data = "Hello, World!"

    # Calculate the hash value using the default algorithm (sha256)
    sha256_hash = calculator.calculate_hash(data)
    print(f"SHA-256 Hash: {sha256_hash}
")

    # Calculate the hash value using the MD5 algorithm
    md5_hash = calculator.calculate_hash(data, 'md5')
    print(f"MD5 Hash: {md5_hash}
")

    # Attempt to calculate the hash value using an unsupported algorithm
    try:
        calculator.calculate_hash(data, 'unsupported_algorithm')
    except ValueError as e:
        print(e)

def __str__(self) -> str:
    return "HashCalculator instance""

def __name__ == "__main__":
    main()
