import random

# List of words to choose from
word_list = ["python", "java", "kotlin", "javascript", "software", "coding", "cloud"]

# Define the Hangman stages for 7 tries
stages = [
    """
    --------
    |      |
    |      
    |     
    |     
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     
    |     
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |      |
    |     
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|
    |     
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |     
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / 
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    |    
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    |    
    |    
    - 
    """
]

def get_word():
    return random.choice(word_list)

def display_hangman(tries):
    return stages[tries]

def play():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0  # Initial number of tries
    max_tries = 7

    print("\nLet's play the Hangman Game!\n")
    print(f"You get {max_tries} tries to guess the correct word!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries < max_tries:
        guess = input("Please guess a letter: ").lower()
        print("\n")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: '{guess}'")
            elif guess not in word:
                print(f"Sorry, the letter '{guess}' is not in the word.")
                guessed_letters.append(guess)
                tries += 1
            else:
                print(f"Good job! '{guess}' is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word: '{guess}'")
            elif guess != word:
                print(f"Oops, '{guess}' is not the word.")
                guessed_words.append(guess)
                tries += 1
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess. Please enter a single letter, or if you know it, guess the word.")
            tries += 1

        print(display_hangman(tries))
        print(word_completion)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"You now have {max_tries - tries} tries left.\n")

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"Yay! Congratulations, you guessed the correct word: '{word}'!")
        print("You win!")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you ran out of tries! The correct word was '{word}'")
        print("Better luck next time!")

if __name__ == "__main__":
    play()
