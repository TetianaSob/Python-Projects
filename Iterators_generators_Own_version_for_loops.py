# Iterators_generators_Own_version_for_loops.py

#for num in [1,2,3]

#for char in "hi there"
'''
def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator)) # h
        except StopIteration:
            print("END OF ITERATOR")
            break

#my_for("hello")

# h
# e
# l
# l
# o
# END OF ITERATOR
'''

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing =next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for([1,2,3,4], print)
# 1
# 2
# 3
# 4

my_for([1,2,3,4,5], square)
# 1
# 2
# 3
# 4
# 1
# 4
# 9
# 16
# 25

#my_for([1,2,3,4], sum)
print("\n")

#my_for("lol", print)
# l
# o
# l