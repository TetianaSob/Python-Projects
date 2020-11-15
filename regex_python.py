#regex_python.py

#import regex module
import re

#define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

#**ex-1
#search a string with our regex
res = pattern.search('Call ne at 415 555-4242!') # <re.Match object; span=(11, 23), match='415 555-4242'>  ###we got a match object
print(res)

#**ex-2
#res = pattern.search("1233323223432htrtgth") # None
#res = pattern.search("42") # None

#**ex-3
res2 = pattern.search('Call ne at 310 445-9876')
print(res2)  # <re.Match object; span=(11, 23), match='310 445-9876'>

print(res2.group()) # '310 334-9876'

#**ex-4
res3 = pattern.search('Call ne at 310 445-9876 or 310 234-9999')
print(res3)  # <re.Match object; span=(11, 23), match='310 445-9876'>

print(res3.group()) # '310 334-9876'
