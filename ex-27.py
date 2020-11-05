artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist['first'] + ' ' + artist['last']
print(full_name) # Neil Young

print("\n")
################

artist = {
    "first": "Neil",
    "last": "Young",
}
 
# concat first and last name with a space
full_name2 = artist["first"] + " " + artist["last"]
print(full_name2)

#################

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name3 = "{} {}".format(artist["first"],artist["last"])
print(full_name3) # Neil Young