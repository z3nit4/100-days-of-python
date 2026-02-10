import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6

# Print logo at start
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ""
for _ in range(word_length):
    display += "_"

print("Word to guess: " + display)

game_over = False
correct_letters = []

while not game_over:

    # Show lives left
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Already guessed check
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("*********************** YOU LOSE ***********************")
            print(f"The word was: {chosen_word}")

    # Win condition
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # Print hangman stage
    print(stages[lives])
