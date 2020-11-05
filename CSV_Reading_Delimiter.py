# CSV_Reading_Delimiter.py

# fighters_2.csv
from csv import reader
with open("fighters2.csv") as file:
    csv_reader = reader(file, delimiter="/")
    for row in csv_reader:
        #each row in list!
        print(row)

# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun_Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']