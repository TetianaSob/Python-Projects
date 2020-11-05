# dictionary_comprehension.py

numbers =  dict(first = 1, second = 2, third = 3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

##############
# Ex

print({num: num**2 for num in [1,2,3,4,5]}) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print("\n")
##############

{num: num**2 for num in [1,2,3,4,5]}
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo) # {'A': '1', 'B': '2', 'C': '3'}

print("\n")
##############

instructor = {
    "name": "Colt",
    "city": "san francisco",
    "color": "purple"
}
yelling_instructor = {k.upper():v.upper() for k, v in instructor.items()}
print(yelling_instructor) # {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

print("\n")
##############

yelling_instructor2 = {(k.upper() if k is 'color' else k): v.upper() for k,v in instructor.items()} # {'A': '1', 'B': '2', 'C': '3'}