# 代码生成时间: 2025-09-20 11:03:28
import scrapy

"""
A simple form data validator using Scrapy framework.
It demonstrates how to validate form data with Scrapy spiders.
"""

class FormValidator:
    """
    Validates form data using various methods.
    """
    def __init__(self):
        # Initialize the validator with default settings
        pass

    def is_valid_string(self, field, length):
        """
        Validates if the string field has the specified length.
        
        Args:
            field (str): The string to validate.
            length (int): The required length of the string.
        
        Returns:
            bool: True if the string is valid, False otherwise.
        """
        if not isinstance(field, str):
            raise ValueError("Field must be a string.")
        return len(field) == length

    def is_valid_email(self, email):
        """
        Validates an email address using a simple regex pattern.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

    def is_valid_phone(self, phone):
        """
        Validates a phone number using a simple regex pattern.
        
        Args:
            phone (str): The phone number to validate.
        
        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        phone_pattern = r"^\+?[1-9]\d{1,14}$"
        return re.match(phone_pattern, phone) is not None

    def validate_form(self, form_data):
        """
        Validates a dictionary of form data.
        
        Args:
            form_data (dict): A dictionary containing form fields and their values.
        
        Returns:
            dict: A dictionary containing validation results for each field.
        """
        results = {}
        for field, value in form_data.items():
            try:
                if isinstance(value, str):
                    if len(value) <= 0:
                        results[field] = False
                        continue
                if field.endswith("_email"):
                    results[field] = self.is_valid_email(value)
                elif field.endswith("_phone"):
                    results[field] = self.is_valid_phone(value)
                elif field.endswith("_name"):
                    results[field] = self.is_valid_string(value, 5)
                else:
                    results[field] = True
            except ValueError as e:
                results[field] = str(e)
        return results

# Example usage
if __name__ == "__main__":
    validator = FormValidator()
    form_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+12345678901",
        "invalid_email": "invalid-email",
        "short_name": "jd"
    }
    results = validator.validate_form(form_data)
    print(results)