# function_built_in_methods_complex_zip.py

#zip()

midterms = [80, 91, 78]
finals = [98,89,53]
students =['dan', 'ang', 'kate']
# print(list(zip(students, midterms, finals))) # [('dan', 80, 98), ('ang', 91, 89), ('kate', 78, 53)]

final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}

scores = map(
    lambda pair: max(pair)
    zip(midterms, finals)
)

print(list(scores))