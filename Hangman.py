import random

def hangman():
    """
    Plays a text-based Hangman game.
    """
    words = ["python", "intern", "program", "coding", "challenge"]
    word_to_guess = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman! 🤠")
    print("Try to guess the word!")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: '{word_to_guess}' 🎉")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess! 👍")
        else:
            print("Sorry, that letter is not in the word. 👎")
            incorrect_guesses += 1
            # Show the final state if this was the last allowed incorrect guess
            if incorrect_guesses == max_incorrect_guesses:
                display_word = ""
                for letter in word_to_guess:
                    if letter in guessed_letters:
                        display_word += letter
                    else:
                        display_word += "_"
                print(f"\nWord: {display_word}")
                print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
                print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    else:
        print("\nGame over! You ran out of guesses. 💀")
        print(f"The word was: '{word_to_guess}'")

if __name__ == "__main__":
    hangman()
