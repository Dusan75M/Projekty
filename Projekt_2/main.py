"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dušan Machů
email: dumadum@centrum.cz
"""

import random
import time

def separator():
    separator = "-" * 47
    return separator

def welcome_prints():
    print("Hi there!", separator(), sep="\n")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.", separator(), sep="\n")
    print("Enter a number:", separator(), sep="\n")

def create_secret_number():
    first_digits = list("123456789")
    first_digit = random.choice(first_digits)
    remaining_digits = list("0123456789")
    remaining_digits.remove(first_digit)
    other_digits = random.sample(remaining_digits, 3)
    return first_digit + ''.join(other_digits)
    
def guess_number():
    return input(">>> ")

def search_faults(entered_number):
    """
    Check whether the input is correct: 4-digit unique number not starting with zero.
    """
    if entered_number.isnumeric():
        if len(entered_number) != 4:
            print("Your guessed number is not 4-digit! Try again: ", separator(), sep="\n")
            return True
        elif entered_number[0] == "0":
            print("Your guess starts with 0! Try again: ", separator(), sep="\n")
            return True
        elif len(entered_number) != len(set(entered_number)):
            print("Your guess includes duplicity! Try again: ", separator(), sep="\n")
            return True
        else:
            return False
    else:
        print("Your guess is not numeric! Try again: ", separator(), sep="\n")
        return True

def game_evaluation(generated_number, entered_number):
    bulls = 0
    cows = 0
    n = 0
    for digit in generated_number:
        if digit == entered_number[n]:
            bulls += 1
            n += 1
        elif digit in entered_number:
            cows += 1
            n +=1
        else:
            n += 1
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow", separator(), sep="\n")
    elif bulls == 1:
        print(f"{bulls} bull, {cows} cows", separator(), sep="\n")
    elif cows == 1:
        print(f"{bulls} bulls, {cows} cow", separator(), sep="\n")
    else:
        print(f"{bulls} bulls, {cows} cows", separator(), sep="\n")

def game_end(guesses_number):
    print("Correct, you've guessed the right number",
          f"in {guesses_number} guesses!", separator(), sep="\n")

def last_exclamation(guesses_number):
    if guesses_number <= 5:
        print("That's amazing!", separator(), sep="\n")
    elif 6 < guesses_number <= 10:
        print("That's very good!", separator(), sep="\n")
    elif 11 < guesses_number <= 15:
        print("That's good!", separator(), sep="\n")
    else:
        print("You should have guessed better!", separator(), sep="\n")

def guess_time(start_time, end_time):
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    print(f"Time to guess: {hours}:{minutes:02}:{seconds:02}")
    
def bulls_cows():
    start_time = time.time()
    game_running = True
    guesses_number = 1

    welcome_prints()

    secret_number = create_secret_number()

    while game_running:
        while True:
        # check the input for faults
            guessed_number = guess_number()
            if not search_faults(guessed_number):
                break
        if secret_number == guessed_number:
            game_running = False
        else:
            game_evaluation(secret_number, guessed_number)
            guesses_number += 1
    else:
        game_end(guesses_number)
        last_exclamation(guesses_number)
    end_time = time.time()
    
    guess_time(start_time, end_time)

if __name__ == "__main__":
    bulls_cows() 