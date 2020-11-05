# ex-71_extract_full_name.py

'''Write a function called extract_full_name. This function should accept a list of dictionaries and 
and return a new list of strings with the first and last name keys in each 
dictionary concatenated.'''

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# def extract_full_name(dict1, dict2):
#     return zip(dict1,
#                map(
#                    lambda pair: max(pair),
#                    zip(dict2)
#                )
#          )

# print(extract_full_name(names) # ['Elie Schoppik', 'Colt Steele'])

'''Extract Full Name Solution
I use map and a lambda to create a new list full of formatted strings:'''

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']