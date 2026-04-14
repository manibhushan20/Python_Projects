import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
guessed_letters = [] # Track EVERYTHING the user types

print(logo)

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # 1. Check if they already tried this letter (right OR wrong)
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try something else!")
        continue # Skip the rest of the loop and ask again
    
    guessed_letters.append(guess)

    # 2. Rebuild the display string
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # 3. Check if the guess was wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # 4. Check if the player won
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])