# 代码生成时间: 2025-08-26 11:08:13
import hashlib


class HashCalculator:
    """
    A simple hash calculator tool to compute hash values of strings.
    Supports various hash algorithms like SHA1, SHA224, SHA256, SHA384, SHA512, etc.
    """

    def __init__(self):
        """
        Initialize the HashCalculator.
        """
        pass

    def calculate_hash(self, input_string, algorithm="sha256"):
        """
        Calculate the hash of the given input string using the specified algorithm.

        Args:
            input_string (str): The string to compute the hash for.
            algorithm (str): The hash algorithm to use (default is 'sha256').

        Returns:
            str: The computed hash in hexadecimal format.

        Raises:
            ValueError: If the algorithm is not supported.
        """
        try:
            hash_obj = getattr(hashlib, algorithm)()
            hash_obj.update(input_string.encode())
            return hash_obj.hexdigest()
        except AttributeError:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    def get_supported_algorithms(self):
        """
        Get a list of supported hash algorithms.

        Returns:
            list: A list of supported hash algorithm names.
        """
        return [attr for attr in dir(hashlib) if attr.startswith('sha')]


# Example usage
if __name__ == "__main__":
    calculator = HashCalculator()
    input_string = "Hello, World!"
    hash_value = calculator.calculate_hash(input_string)
    print(f"The hash of '{input_string}' is: {hash_value}")
    print(f"Supported algorithms: {calculator.get_supported_algorithms()}")