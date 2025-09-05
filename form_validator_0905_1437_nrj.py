# 代码生成时间: 2025-09-05 14:37:25
# -*- coding: utf-8 -*-

"""
Form Data Validator using Scrapy framework.
This script serves as a form data validator that checks if the input data meets
the specified criteria.
"""

import scrapy
from scrapy.exceptions import DropItem
from scrapy.item import Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

# Define the fields for the item that will be validated
class FormItem(scrapy.Item):
    name = Field()
    email = Field()
    age = Field()

# Define the validators
def validate_name(value):
    """
    Validate the name field.
    Ensure the value is not empty and is a string.
    """
    if not value or not isinstance(value, str):
        raise DropItem('Invalid name')
    return value

def validate_email(value):
    """
    Validate the email field.
    Ensure the value is not empty, is a string, and contains an '@' symbol.
    """"
    if not value or not isinstance(value, str) or '@' not in value:
        raise DropItem('Invalid email')
    return value

def validate_age(value):
    """
    Validate the age field.
    Ensure the value is a positive integer.
    """"
    try:
        age = int(value)
        if age <= 0:
            raise DropItem('Age must be a positive integer')
    except ValueError:
        raise DropItem('Invalid age')
    return age

# Define the item loader for the form item
class FormLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    name_in = MapCompose(validate_name)
    email_in = MapCompose(validate_email)
    age_in = MapCompose(validate_age)

    def __init__(self, *args, **kwargs):
        super(FormLoader, self).__init__(FormItem, *args, **kwargs)
        self.processors['name'] = self.name_in
        self.processors['email'] = self.email_in
        self.processors['age'] = self.age_in

# Example usage of the form validator
def process_form_data(form_data):
    """
    Process the form data using the FormLoader.
    """
    loader = FormLoader(item=FormItem(), response=form_data)
    loader.add_value('name', form_data.get('name'))
    loader.add_value('email', form_data.get('email'))
    loader.add_value('age', form_data.get('age'))
    return loader.load_item()

# Example form data
form_data_example = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'age': '30'
}

# Process the example form data
try:
    validated_data = process_form_data(form_data_example)
    print('Validated Data:', validated_data)
except DropItem as e:
    print('Error:', e.value)