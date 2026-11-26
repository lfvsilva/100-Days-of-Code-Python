# Display art
from art import logo, vs
from game_data import data
import random
import subprocess

def print_info(option):
    if option['description'][0].lower() in "aeiou": 
        article = "an"
    else:
        article = "a"

    return(f"{option['name']}, {article} {option['description']}, from {option['country']}")

def compare(data):
    playing = True
    player_score = 0
    a = random.choice(data)
    data.remove(a)
    b = random.choice(data)
    data.remove(b)
    while playing:    
        subprocess.call("cls||clear", shell=True)
        print(logo)
        if player_score > 0:
            print(f"You're right! Current score: {player_score}")

        print(f"Compare A: {print_info(a)}")

        print(vs)

        print(f"Compare B: {print_info(b)}")

        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == 'a':
            playing = a['follower_count'] == max(a['follower_count'], b['follower_count'])
            if playing:
                b = random.choice(data)
                data.remove(b)
                player_score += 1
        if player_choice == 'b':
            playing = b['follower_count'] == max(a['follower_count'], b['follower_count'])
            if playing:
                a = b
                b = random.choice(data)
                data.remove(b)
                player_score += 1
        else:
            subprocess.call("cls||clear", shell=True)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {player_score}")
            return

compare(data=data)


