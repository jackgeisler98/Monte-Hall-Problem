#Jack Geisler Monte Hall Problem 
import random
keep_choice = 0
change_choice = 0
for i in range (1,10001):
    prize_location = random.randrange(1,4)
    player_choice = random.randrange(1,4)
    if prize_location == player_choice:
        keep_choice = keep_choice + 1
    elif prize_location != player_choice:
        change_choice = change_choice + 1
print(keep_choice/100)
print(change_choice/100)