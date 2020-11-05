# Loop over donations, add all the VALUES together and store in a variable 
# called total_donations

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
 
total_donations = 0
 
for donation in donations.values():
 total_donations += donation
print(donations) 

# {'sam': 25.0, 'lena': 88.99, 'chuck': 13.0, 'linus': 99.5, 'stan': 150.0, 'lisa': 50.25, 'harrison': 
#10.0}

