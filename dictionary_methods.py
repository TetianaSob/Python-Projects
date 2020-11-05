# dictionary_methods.py

# clear method
d = dict(a=1, b=2, c=3)
d.clear()
print(d) # {}

# copy method
d1 = dict(a=1, b=2, c=3)
c = d1.copy()
print(c) # {'a': 1, 'b': 2, 'c': 3}
print(c is d) # False 
print(c == d) # False

# fromkeys method
print("\n")
 
print({}.fromkeys("a", "b")) # {'a': 'b'}
print({}.fromkeys(["email"], 'unknown')) # {'email': 'unknown'}
print({}.fromkeys("a", [1,2,3,4,5])) # {'a': [1, 2, 3, 4, 5]}
 
print("\n")
##############

new_user = {}.fromkeys([])
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user) # {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}

print("\n")

new_user.fromkeys(range(1,10), 'unknown')
print(new_user) # {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}

#get method

d = dict(a=1, b=2, c=3)
print(d['a']) # 1
print(d.get('a')) # 1

print("\n")

print(d.get('b')) # 2
print(d['no_key']) # no_key'

