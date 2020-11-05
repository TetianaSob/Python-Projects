# CSV_File_DictWiriter.py

from csv import writer, DictWriter

with open("cat.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })
