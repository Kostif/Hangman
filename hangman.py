import random
from words import words
import string
import os

game = True

def player_guess():     # Ask user input check, if it's in the alphabet and store it in used_letters

    guess = ''
    while guess not in all_letters:
        
        guess = (input('Please guess a letter')).lower()
        
        if guess in used_letters:
            print("You have already used that letter")
            guess = ''
            continue
            

    used_letters.add(guess)

    return guess

def guess_check(guess,lives):     #Checks if user's guess is in the word and replaces the '_' in word_display to display the current state to the user

    if guess not in current_word:
        lives -= 1
        print('Wrong!')
    else:
        for i in range(len(current_word)):
            if guess == current_word[i]:
                word_display[i] = guess
        print("Correct!")
    
    return lives

def win_check(current_word,word_display):

    guessed_word = ''.join(word_display)

    if guessed_word == current_word:
        print("Congratulations you have won!")
        check = True
    else:
        check = False

    return check

while game == True:

    #Setting starting values of player lives, generating random word, creating set of all letters, empty set for player guesses, and a display for the user
    #And a value to see if the games is won

    won = False
    lives = 5
    current_word = random.choice(words)
    all_letters = set(string.ascii_lowercase)
    used_letters = set()
    word_display = list(('_')*len(current_word))
    replay = ''
    input('Welcome to hangman! Press any key to continue.')

    while lives != 0 and won == False:
        
        print(f"Good luck! {word_display}  {lives} lives.")
        guess = player_guess()
        os.system('clear')
        print(f"You have used these letters {used_letters}.")

        lives = guess_check(guess,lives)
        won = win_check(current_word,word_display)

    if lives ==0 :
        print("I am sorry you have lost.")    

    while replay != 'y' or 'n':
        replay = input('Do you want to play again? Y/N').lower()
        if replay == 'n':
            print("Thanks for playing!")
            game = False
            break
        else:
            break