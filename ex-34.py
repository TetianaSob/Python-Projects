#ex-34.py

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {key: '0' for key in 'eaiou'}
print(answer) # {'e': '0', 'a': '0', 'i': '0', 'o': '0', 'u': '0'}

print("\n")
##########

answer2 = {char:0 for char in 'aeiou'}
print(answer2) # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

print("\n")
##########

answer3 = dict.fromkeys("aeiou", 0)
print(answer3) # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

