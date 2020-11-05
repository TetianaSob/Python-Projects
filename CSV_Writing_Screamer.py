# CSV_Writing_Screamer.py

from csv import reader, writer

with open("fighters_2.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    # for row in fighters:
    #     print(row)

with open('screaming_flights.csv', "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# ['NAME|COUNTRY|HEIGHT (IN CM)']
# ['RYU|JAPAN|175']
# ['KEN|USA|175']
# ['CHUN_LI|CHINA|165']
# ['GUILE|USA|182']
# ['E. HONDA|JAPAN|185']
 
# option 2

with open("fighters_2.csv") as file:
    csv_reader = reader(file)
    with open('screaming_flights3.csv', "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])