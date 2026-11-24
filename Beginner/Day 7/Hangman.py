import random
stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
"""

  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 0

while not game_over:
    print(stages[lives])
    print(f"**** {len(stages) - 1 - lives} LIVES LEFT ****")
    guess = input("Guess a letter: \n").lower()
    if guess in chosen_word:
        print("Right\n")
        correct_letters.append(guess)
        aux = list(placeholder)
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:
                aux[i] = guess
        placeholder = "".join(aux)
    else:
        lives += 1
        print("Wrong\n")

    print(stages[lives])
    print(placeholder)
    if not "_" in placeholder:
        print("**** YOU WIN *****")
        game_over = True
    elif lives >= (len(stages)-1):
        print("**** YOU LOSE ****")
        game_over = True
    

