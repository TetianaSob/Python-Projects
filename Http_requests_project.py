# Http_requests_project.py

import requests
from random import choice

print("DAD JOKE")

user_input = input("What would you like to searh for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
print(res)

print("\n")

#print(len(res["results"])) # 10
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}")
    print(choice(results)['joke'])
elif  num_jokes == 1:
    print("THERE IS ONE JOKE!")
    print(results[0]['joke'])
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}!")

## dod
## -> I found 12 about dog
##“My Dog has no nose.” “How does he smell?” “Awful”



'''
What would you like to searh for? red
{'current_page': 1, 'limit': 20, 'next_page': 2, 'previous_page': 1, 'results': 
[{'id': 'xXSv492wPmb', 'joke': 'What is red and smells like blue paint?\r\nRed paint!'}, 
{'id': 'PucUvXSvkqc', 'joke': 'Why did the fireman wear red, white, and blue 
suspenders? To hold his pants up.'}, {'id': 'JeF69xAQSnb', 'joke': 'A red and a blue ship 
have just collided in the Caribbean. Apparently the survivors are marooned.'}, 
{'id': 'haahVKZDtrc', 'joke': "What's red and bad for your teeth? A Brick."},nGJtPuc', 
'joke': 'Why is the new Kindle screen textured to look like paper? So you feel write at home.'}, 
{'id': 'CAlG6MRnWnb', 'joke': 'I just got fired from a florist, apparently I took too many 
leaves.'}, {'id': 'lV8hqHexHBd', 'joke': 'Why did the worker get fired from the orange 
juice factory? Lack of concentration.'}, {'id': '9pW8xXgiiqc', 'joke': "I considered 
building the patio by myself. But I didn't have the stones."}, {'id': 'IYT082EQukb', 
'joke': 'Why was ten scared of seven? Because seven ate nine.'}, {'id': 'tHJtrrzP7wc', 
'joke': 'Mahatma Gandhi, as you know, walked barefoot most of the time, which produced 
an impressive set of calluses on his feet. \r\nHe also ate very little, which made him 
rather frail and with his odd diet, he suffered from bad breath. \r\nThis made him a super 
calloused fragile mystic hexed by halitosis.'}, {'id': '7Uvc29hFIBd', 'joke': "Why are 
mummys scared of vacation? They're afraid to unwind."}, {'id': 'DIeFtkVvHlb', 
'joke': "Why do valley girls hang out in odd numbered groups? Because they can't even."}, 
{'id': 'QnWnWSfiqc', 'joke': "Why can't a bicycle stand on its own? It's two-tired."}, 
{'id': 'eiyAXnWS0g', 'joke': "The biggest knight at King Arthur's round table was Sir 
Cumference. He acquired his size from eating too much pi."}, {'id': 'Qusrcahiib', 
'joke': 'Astronomers got tired watching the moon go around the earth for 24 hours. 
They decided to call it a day.'}, {'id': 'ucxPZDAlGlb', 'joke': 'If two vegans are 
having an argument, is it still considered beef?'}, {'id': '0189hNRf2g', 'joke': "I'm 
tired of following my dreams. 
I'm just going to ask them where they are going and meet up with them later."}, 
{'id': 'NCAIYLeNe', 'joke': 'I fear for the calendar, its days are numbered.\n'}, 
{'id': '218xkq49prc', 'joke': "I was fired from the keyboard factory yesterday.  
I wasn't putting in enough shifts."}], 'search_term': 'red', 'status': 200, 'total_jokes': 26, 
'total_pages': 2}'''



