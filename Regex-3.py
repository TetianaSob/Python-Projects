#Regex-3.py

import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("https://www.my-website.com/bio?data=blah&cat=yes")

print(match.group()) # http://www.youtube.com/videos
print("\n")
print(match.groups()) # ('http', 'www.youtube.com/videos')

print("\n")
print(match.group(0)) # http://www.youtube.com/videos
print(match.group(1)) # http
print(match.group(2)) # www.youtube.com
print(match.group(3)) # /videos

print("\n")
print(f"Protocol: {match.group(1)}") # Protocol: http
print(f"Domain: {match.group(2)}") # Domain: www.my-website.com
print(f"Everything Else: {match.group(3)}") # Everything Else: /bio?data=blah&cat=yes

print("\n")
# to match everything
print(match.group()) # https://www.my-website.com/bio?data=blah&cat=yes

print("\n")
# to match everything
print(match.groups()) # ('https', 'www.my-website.com', '/bio?data=blah&cat=yes')