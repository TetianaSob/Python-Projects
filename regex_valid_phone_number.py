# regex_valid_phone_number.py
import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)

print(extract_all_phones("my number is 432 567-8976 or call me at 614 300 3021"))  # ['432 567-8976']
print(extract_all_phones("my number is 432 567"))  # []
#
#print(extract_all_phones("my number is  432 567-8976")) # 432 567-8976
#print(extract_all_phones("my number is  432 567-8976434")) # None
#print(extract_all_phones("432 567-8976434")) # None
#print(extract_all_phones("432 567-8976 my phone number")) # 432 567-8976
#print(extract_all_phones("432 567-8976 my phone number")) 
# \b - the bounndery character
print("\n")

def is_valid_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return None

print(is_valid_phone("432 567-8976")) # True
print(is_valid_phone("432 567-8976 ads")) # None
print(is_valid_phone("asd 432 567-8976 d")) # None

'''
def is_valid_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

'''