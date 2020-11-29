# Regex_names.py

import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
pattern.sub("REDACTED", text)

print(pattern.search(text).group()) # Mrs. Daisy

print("\n")

text2 = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result2 = pattern.sub("REDACTED", text2)

print(result2) # Last night REDACTED and REDACTED murdered REDACTED

print("\n")

text3 = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result3 = pattern.sub("\g<1>REDACTED", text3)

print(result3) # Last night Mrs.REDACTED and Mr.REDACTED murdered Ms.REDACTED
