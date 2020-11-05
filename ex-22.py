answer = [num for num in range(1,101) if num % 12 == 0]
print(answer) # [12, 24, 36, 48, 60, 72, 84, 96]

# answer = [val for val in range(1,101) if val % 12 == 0] 

# answer = [char for char in "amaizing" if char not in "aeiou"])

answer2 = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 
print(answer2) # ['m', 'z', 'n', 'g']