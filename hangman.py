import random

words = ["python", "computer", "programming",
         "keyboard", "developer"]

TEST_MODE = True

if TEST_MODE:
    secret_word = "python"
else:
    secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while wrong_guesses < max_attempts:

    progress = ""

    for letter in secret_word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "

    print("\nProgress:", progress)

    if all(letter in guessed_letters for letter in secret_word):
        break

    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Invalid input. Enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(guess + ": Correct")
    else:
        wrong_guesses += 1
        print("Wrong guess:", wrong_guesses, "/", max_attempts)

if all(letter in guessed_letters for letter in secret_word):
    print("\nYou won! The word was", secret_word)
else:
    print("\nGame Over! The word was", secret_word)

print("Wrong guesses:", wrong_guesses, "/", max_attempts)
