# 代码生成时间: 2025-08-18 07:46:54
import scrapy
def is_valid_url(url):
    """
    Validate if the given URL is valid and reachable.
    
    Args:
    url (str): The URL to validate.
    
    Returns:
    bool: True if the URL is valid and reachable, False otherwise.
    """
    try:
        # Check if the URL is valid using scrapy's request method
        response = scrapy.Request(url, callback=lambda x: x)
        # Send the request and check if the status code is 200
        yield scrapy.Request(url, callback=lambda x: x)
        response = yield response
        if response.status == 200:
            return True
        else:
            return False
    except Exception as e:
        # If any error occurs, log the error and return False
        print(f"Error validating URL: {e}")
        return False

# Example usage
if __name__ == '__main__':
    url_to_test = "http://example.com"
    if is_valid_url(url_to_test):
        print(f"The URL {url_to_test} is valid and reachable.")
    else:
        print(f"The URL {url_to_test} is not valid or not reachable.")