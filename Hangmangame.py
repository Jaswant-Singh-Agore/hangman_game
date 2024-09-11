from words import word_list
from logo import hangman_art

import random
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)

for _ in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_words = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()



    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_words.append(guess)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"
    print(display)
    
            

    if guess not in chosen_word:
        lives -= 1
        print(f"--------------remaining={lives}-----------------------------")
        if lives == 0:
            game_over = True
            print("You lose😔😔")
    
    if "_" not in display:
        game_over = True
        print("You Win😁😄")
        
        

