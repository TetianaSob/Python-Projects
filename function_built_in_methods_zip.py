# function_built_in_methods_zip.py

# zip()

first_zip = zip([1,2,3], [4,5,6])
#print(list(first_zip)) # [(1, 4), (2, 5), (3, 6)]

print(dict(first_zip)) # {1: 4, 2: 5, 3: 6}

print("\n")
##########

# nums1 = [1,2,3,4,5]
# nums2 = [6,7,8,9,10]
# print(list(zip(nums1, nums2))) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
z = dict(zip(nums1, nums2))
print(z) # {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

####

z = dict(zip(nums2, nums1))
print(z) # {6: 1, 7: 2, 8: 3, 9: 4, 10: 5}

print("\n")
####

words = ['hi', 'lol', 'haha', ':)']
print(list(zip(words, nums1,nums2))) # [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)]

print("\n")
####

five_by_two = [(0, 1), (1, 2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two))) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

