# Ex-66_Build_in methods.py

'''Greatest Magnitude Exercise

Write a function 'max_magnitude' that accepts a single list
dull of number. It should return the magnitude of the largest
magnitude ( the number that is furthest way from zero).'''
'''max_magnitude([300, 20, -900])'''
'''max_magnitude([10, 11, 12)'''

def max_magnitude(nums):
    return max(abs(num) for num in nums)
    
print(max_magnitude([300,20,-900])) # 900

''' Greatest Magnitude Solution 
To find the greatest magnitude (the greatest distance from 0), I combine max() and abs()
I call abs() on each num, and find the maximum resulting value using max()
'''

def max_magnitude2(nums):
    return max(abs(num) for num in nums)

print(max_magnitude2([300,20,-800])) # 800

