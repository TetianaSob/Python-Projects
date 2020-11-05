# CSV_Writing.py

#  writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV

from csv import writer

with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])

# Name,Age

# Blue,3

# Kitty,1
    
