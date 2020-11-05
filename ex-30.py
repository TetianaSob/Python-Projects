#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys("game_properties", 0)
#print(initial_game_state) # {'g': 0, 'a': 0, 'm': 0, 'e': 0, '_': 0, 'p': 0, 'r': 0, 'o': 0, 't': 0, 'i': 0, 's': 0}

game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)

print(game_properties) # ['current_score', 'high_score', 'number_of_lives', 'items_in_inventory', 'power_ups', 'ammo', 'enemies_on_screen', 'enemy_kills', 'enemy_kill_streaks', 'minutes_played', 'notifications', 'achievements']
print("\n")
print(initial_game_state) 
# {'current_score': 0, 'high_score': 0, 'number_of_lives': 0, 'items_in_inventory': 0, 'power_ups': 0, 
# 'ammo': 0, 'enemies_on_screen': 0, 'enemy_kills': 0, 'enemy_kill_streaks': 0, 'minutes_played': 0, 'notifications': 0, 'achievements': 0}
