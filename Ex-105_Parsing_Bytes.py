# Ex-105_Parsing_Bytes.py

'''Write a function called 'parse_bytes' that accepts a single string. It should return 
a list of a binary bytes contained in the string. Each byte is just a combination of 
eight 1's or 0's. For example:

parse_bytes("11010101 101 323")
parse_bytes("my data is: 10101010 11100010")
parse_bytes("asdsa")
'''
# Hint: take advantage of '\b\ Not all bytes will have a space before and after, some 
# come at the beginning of a file or at the end. Use findall!

'''Parsing Bytes Solution
My regex looks like this: '\b[10]{8}\b'   It consists of eight 1s or 0s, surrounded by word boundaries on either side.  Remember a word boundary is either a space or the start/end of a line.

I then used findall  rather than search, to return a list of all matches.  Here's the final solution:
'''


import re
 
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results

print(parse_bytes("11010101 101 323")) # ['11010101']
print(parse_bytes("my data is: 10101010 11100010")) # ['10101010', '11100010']
print(parse_bytes("asdsa")) # []