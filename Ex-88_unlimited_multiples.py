# Ex-88_unlimited_multiples.py

''' Write a function called 'get_unlimited_multiples', which accepts a number
and returns a generator that will yield an unlimited number of the multiples
of that number.

The default number should be 1.

sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

# SOLUTION
# Get Unlimited Multiples Solution
# This is similar to previous exercise, except it's simpler! We just loop forever (while True) instead of checking to see how many times we've looped.

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num

sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)]) # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]
print([next(sevens) for i in range(5)]) # [112, 119, 126, 133, 140]