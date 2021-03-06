# Http_requests_params.py

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)

print(response) # <Response [200]>

data = response.json()
#print(dict(data))

''' {'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 
'results': [{'id': 'iGJeVKmWDlb', 'joke': 'My cat was 
just sick on the carpet, I don’t think it’s feline well.'}, {'id': '8UnrHe2T0g', 
'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'daaUfibh', 
'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, 
{'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, 
{'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, 
{'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She 
was a roman catholic.'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of 
disorganized cats? A cat-tastrophe.'}, 
{'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost 
stepped in a poodle.'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? 
Because he was trying to catch up on his sleep!'}, {'id': '1wkqrcNCljb', 
'joke': "Did you know that protons have mass? I didn't even know they were catholic."}], 
'search_term': 'cat', 'status': 200, 'total_jokes': 10, 'total_pages': 1}'''

######
print("\n")
print((data["results"]))

######
print("\n")
print(dict(data))

'''{'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 
'results': [{'id': 'iGJeVKmWDlb', 'joke': 'My cat was 
just sick on the carpet, I don’t think it’s feline well.'}, {'id': '8UnrHe2T0g', 
'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'daaUfibh', 
'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, 
{'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, 
{'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, 
{'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She 
was a roman catholic.'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of 
disorganized cats? A cat-tastrophe.'}, 
{'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost 
stepped in a poodle.'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? 
Because he was trying to catch up on his sleep!'}, {'id': '1wkqrcNCljb', 
'joke': "Did you know that protons have mass? I didn't even know they were catholic."}], 
'search_term': 'cat', 'status': 200, 'total_jokes': 10, 'total_pages': 1}
'''

#print(data["joke"])

########
#print("\n")

#print(f"status: {data['status']}")