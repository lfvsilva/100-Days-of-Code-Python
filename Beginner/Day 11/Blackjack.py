import random
import subprocess
from art import logo

hands = {
    "Player": {"Hand": [], "score": 0},
    "Computer": {"Hand": [], "score": 0}
}

def clear_hands():
    hands["Player"]["Hand"].clear()
    hands["Computer"]["Hand"].clear()

def draw_card(qty, dictionary):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dictionary["Hand"].extend(random.choices(population=cards, k=qty))
    update_hand_score(dictionary)

def update_hand_score(dictionary):
    dictionary["score"] = sum(dictionary["Hand"])

def computer_game():
    player_score = hands["Player"]["score"]
    while hands["Computer"]["score"] <= player_score and hands["Computer"]["score"] < 18:
        draw_card(1, hands["Computer"])
    if hands["Computer"]["score"] > player_score:
        return True
    elif hands["Computer"]["score"] > 21:
        return False
    else:
        return False

def start_game():
    draw_card(2, hands["Player"])
    draw_card(1, hands["Computer"])


wanna_play = True
while wanna_play:
    wanna_play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower() == "y"
    if not wanna_play:
        break
    clear_hands()
    subprocess.call("cls||clear", shell=True)
    print(logo)

    start_game()
    playing_game = True
    while playing_game:
        print(f"Your cards: {hands["Player"]["Hand"]}, current score: {hands["Player"]["score"]}")
        print(f"Computer's first card: {hands["Computer"]["Hand"][0]}")
        if hands["Player"]["score"] == 21:
            print("Win with a Blackjack.")
            break
        elif hands["Player"]["score"] > 21:
            print("You went over. You lose")
            break
        else:
            new_card = input("Type \'y\' to get another card, type \'n\' to pass: ").lower() == "y"
            if new_card:
                draw_card(1, hands["Player"])
            else:
                computer_win = computer_game()
                break

    print(f"Your final hand: {hands["Player"]["Hand"]}, final score: {hands["Player"]["score"]}")
    print(f"Computer's final hand: {hands["Computer"]["Hand"]}, final score: {hands["Computer"]["score"]}")
    if computer_win:
        print("You lose")
    elif hands["Player"]["score"] == hands["Computer"]["score"]:
        print("It's a Draw")
    else:
        print("You Win!")


    