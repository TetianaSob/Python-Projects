# List Comprehansion

numbers = [1,2,3,4,5,6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(evens) # [2, 4, 6]
print(odds) # [1, 3, 5]

numb = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(numb) # [0.5, 4, 1.5, 8, 2.5, 12]