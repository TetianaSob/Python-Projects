# CSV_Reading.py
from csv import reader

#to read the file
# each row is an ordered list
with open("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        #each row is a list
        print(row)

# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun_Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
print("\n")

with open("fighters.csv") as file:
    csv_reader = reader(file)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        #each row is a list
        #print(row)

# Name is from Country
# Ryu is from Japan
# Ken is from USA
# Chun_Li is from China
# Guile is from USA
# E. Honda is from Japan

print("\n")

# to take out the first row and start reading from the second row
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

# Ryu is from Japan
# Ken is from USA
# Chun_Li is from China
# Guile is from USA
# E. Honda is from Japan

print("\n")

# to print as a list

with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

# [['Name', 'Country', 'Height (in cm)'], 
# ['Ryu', 'Japan', '175'], 
# ['Ken', 'USA', '175'], 
# ['Chun_Li', 'China', '165'], 
# ['Guile', 'USA', '182'], 
# ['E. Honda', 'Japan', '185']]    


######## Dict

# to read dict
# each row is an ordered dict
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each row is a list
        print(row)

# {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
# {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'}
# {'Name': 'Chun_Li', 'Country': 'China', 'Height (in cm)': '165'}
# {'Name': 'Guile', 'Country': 'USA', 'Height (in cm)': '182'}
# {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm)': '185'}

print("\n")

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each row is a list
        print(row['Name'])

# Ryu
# Ken
# Chun_Li
# Guile
# E. Honda

print("\n")