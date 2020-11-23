# Regex_compilation_flags.py
import re

#pat = re.compile(r'^(a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pattern = re.compile(r""""
    ^([A-Za-z0-9_\.-]+) # this is a part of the email
    @                # single # sign
    ([0-9A-Za-z\.-]+)   # email provider
    \.               # single period
    ([A-Za-z\.]{2,6})$  # com, org, net, etc.
""", re.X, re.IGNORECASE)

match = pattern.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())