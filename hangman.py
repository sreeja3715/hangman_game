import random

word_list = ["python", "apple", "chair", "tiger", "phone"]
word = random.choice(word_list)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    guess = input("Enter a letter: ").lower()

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

if attempts == 0:
    print("Game Over! The word was:", word)