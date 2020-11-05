# append_files_blocks.py

with open("haiku.txt", "a") as file:
    file.seek(0)
    file.write("APPENDING!!! :)")

# Here's one more haiku
# What about the older one?
# Let's go check it out!Here's one more haiku
# What about the older one?
# Let's go check it out!APPENDING!!!APPENDING!!!

# to read and write the file

with open("haiku.txt", "r+") as file:
    file.write("ADDED USING" "r+")

# ADDED USING r+e haiku
# What about the older one?
# Let's go check it out!Here's one more haiku
# What about the older one?
# Let's go check it out!APPENDING!!!APPENDING!!!APPENDING!!! :)APPENDING!!! :)APPENDING!!! :)

with open("haiku.txt", "r+") as file:
    file.write(";)" "r+")
    file.seek(10)
    file.write(":(")