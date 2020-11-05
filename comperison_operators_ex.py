
name = 'colt'
print([char.upper() for char in name]) # ['C', 'O', 'L', 'T']

###########

friends = ['ashley', 'matt', 'michael']
print([friend[0].upper() for friend in friends]) # ['A', 'M', 'M']

###########

print([num*10 for num in range(1,6)]) # [10, 20, 30, 40, 50]

###########

print([bool(val) for val in [0, [], '']])  # [False, False, False]

###########

print(bool('')) # False

###########

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indogo', 'violet']
print([color.upper() for color in colors]) # ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDOGO', 'VIOLET']

###########

nums = [1,2,3]
print([str(num) for num in nums]) # ['1', '2', '3']

