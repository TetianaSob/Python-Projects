# Ex-97_statistics.py

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

#Statistic Exercise Solution


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

print(statistics('story.txt')) # {'lines': 6, 'words': 13, 'characters': 68}
