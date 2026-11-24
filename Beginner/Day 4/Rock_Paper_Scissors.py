import random


def checkWinner(choice, computer_choice):
    if choice == computer_choice:
        return "Draw"
    else:
        if (choice == rock and computer_choice == scissors) or (choice == paper and computer_choice == rock) or (choice == scissors and computer_choice == paper):
            return  ("You Win")
        else:
            return ("You Lose")
    


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[choice])
print("Computer chose: ")
computer_choice = random.choice(options)
print(computer_choice)

print(checkWinner(options[choice], computer_choice))



