# Lambda_built_in_functions.py

# all
print(all([0,1,2,3])) # False

print("\n")

print(all([char for char in 'eio' if char in 'aeiou'])) # True

print("\n")

print(all([num for num in [4,2,10,6,8] if num % 2 == 0])) # True

print("\n")
############
print("Example 2")

people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
print(all([name[0] == 'C' for name in people])) # True

####
print("\n")

people.append("Kristy")
print(all([name[0] == 'C' for name in people])) # False

print("\n")
############
print("Example 3")

nums = [2,60,26,18]
print(all([num % 2 == 0 for num in nums])) # True

####
nums.append(1)
print(all([num % 2 == 0 for num in nums])) # False