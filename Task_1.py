import random

# Predefined list of 5 words
words = ["python", "developer", "code", "hangman", "programming"]

def play_hangman():
    secret_word = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    word_guessed = False

    print("Welcome to Hangman!")

    # Game loop
    while incorrect_guesses < max_incorrect and not word_guessed:
        # Display the current word state (e.g., p y _ _ o n)
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("\nWord: " + " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")

        # Check if the player has guessed all letters
        if "_" not in [letter if letter in guessed_letters else "_" for letter in secret_word]:
            word_guessed = True

    # Win/Loss outcome
    if word_guessed:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
    else:
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()