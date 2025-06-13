import random

# List of words for the game
word_list = ["python", "hangman", "programming", "developer", "algorithm", "technology", "stack", "project", "web"]

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []
tries = 6  # Total attempts

# Function to display the word with underscores and guessed letters
def display_word():
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Game Start
print("Welcome to Hangman!")

while tries > 0:
    print("\nWord:", display_word())
    print(f"Tries left: {tries}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct!")
        if all(letter in guessed_letters for letter in chosen_word):
            print("\nCongratulations! You guessed the word:", chosen_word)
            break
    else:
        print("Wrong guess.")
        tries -= 1

if tries == 0:
    print("\nGame over! The word was:", chosen_word)
