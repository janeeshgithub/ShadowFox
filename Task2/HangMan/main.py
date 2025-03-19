import json
import random

# Hangman ASCII Art
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def load_words():
    """Load words and hints from the JSON file."""
    try:
        with open("words.json", "r") as file:
            data = json.load(file)
        return data["words"]
    except FileNotFoundError:
        print("Error: 'words.json' file not found!")
        exit()

def choose_word(word_list):
    """Select a random word and its hint."""
    word_entry = random.choice(word_list)
    return word_entry["word"], word_entry["hint"]

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    words = load_words()
    word, hint = choose_word(words)
    guessed_letters = set()
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("🎉 Welcome to Hangman! 🎉")
    print(f"Hint: {hint}")

    while attempts < max_attempts:
        print(HANGMAN_PICS[attempts])
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts += 1
            print("❌ Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print(HANGMAN_PICS[attempts])
        print("💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
