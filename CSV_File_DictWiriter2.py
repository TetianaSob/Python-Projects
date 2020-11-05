# CSV_File_DictWiriter2.py

from csv import DictReader, DictWriter

def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighters_2.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters_2.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": f["Height (in cm)"]
        })

#[{'Name|Country|Height (in cm)': 'Ryu|Japan|175'}, {'Name|Country|Height (in cm)': 'Ken|USA|175'}, {'Name|Country|Height (in cm)': 'Chun_Li|China|165'}, {'Name|Country|Height (in cm)': 'Guile|USA|182'}, {'Name|Country|Height (in cm)': 'E. Honda|Japan|185'}]