import itertools
import random

word_list = ["bank"]
random.shuffle(word_list)
chosen_word = word_list[0]
incorrect_count = 0
correct_count = 0

for checking in itertools.count():
    guess = input("Enter a letter as your guess: ")
    if guess in chosen_word:
        print(f"Correct! The letter {guess} is in the word.")
        correct_count += 1
        if correct_count == len(chosen_word):
            print(f"Congratulations! You've guessed the word: {chosen_word}")
            break
        else:
            continue
    else:
        print(f"Wrong! The letter {guess} is not in the word.")
        incorrect_count += 1

        if incorrect_count == 6:
            print("Game Over, You Lose!")
            break