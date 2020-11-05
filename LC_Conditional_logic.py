#LC with Conditional Logic

numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0]
print(evens) # [2, 4, 6] 
odds = [num for num in numbers if num % 2 != 0]
print(odds) # [1, 3, 5]

#############

print([num*2 if num % 2 == 0 else num/2 for num in numbers]) # [0.5, 4, 1.5, 8, 2.5, 12]

#############

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels  if char not in "aeiou")) # Ths s s mch fn!

##########

print('....'.join(["cool", "dude"])) # cool....dude