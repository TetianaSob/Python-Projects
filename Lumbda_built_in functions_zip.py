# Lumbda_built_in functions_zip.py

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades) # [98, 91, 78]

final_grages = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grages) # {'dan': 98, 'ang': 91, 'kate': 78}

scores =zip(
            students,
            map(
                lambda pair: max(pair),
                zip(midterms, finals)
            )
        )


print(dict(scores)) # {'dan': 98, 'ang': 91, 'kate': 78}

print("\n")

# average grades
avg_grades =zip(
            students,
            map(
                lambda pair: ((pair[0]+pair[1])/2),
                zip(midterms, finals)
            )
        )


print(dict(avg_grades)) # {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}