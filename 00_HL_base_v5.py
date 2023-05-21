# Imports
import math
import random


# Functions

def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


def statement_generator(statement, decoration):
    middle = f'{decoration.upper() * 3} | {statement}! | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


def int_check(question, low_num=None, high_num=None, exit_code=None):
    situation = ""
    if low_num is not None and high_num is not None:
        situation = "both"
    elif low_num is not None and high_num is None:
        situation = "low only"

    while True:

        # ask the user the question
        response = input(question)

        # if they put in the exit code, return it.
        if response == exit_code:
            print("Closing... 👋")
            exit()
        # if they have not put in the exit code, check they have valid number
        try:
            response = int(response)
            if situation == "both":

                if response < low_num or response > high_num:
                    print(f"Please enter a number between {low_num} and {high_num}")

                    continue

            elif situation == "low only":
                if response < low_num:
                    print(f"Please enter a number that is more than (or equal to) {low_num}")
                    continue

            return response

        except ValueError:
            print("Please enter an integer")


# Variables

already_guessed = []
all_round_wins = []
play_again = "yes"
times_won = 0
won = False
result = ""
rounds = 0
guess = ""

# default values
minimum = 0
maximum = 100

choose_params = "yes"

while play_again == "yes":

    if rounds > 0:
        choose_params = yes_no("The current game asks users to guess a "
                               f"number between {minimum} and {maximum}.   "
                               f"Do you want to "
                               "change this?")

    if choose_params == "yes":
        minimum = int_check("Choose a low number: ", low_num=None, high_num=None, exit_code="xxx")
        maximum = int_check("Choose a high number", minimum + 1)

    # calculate maximum number of guesses needed
    fixed_range = maximum - minimum + 1
    max_raw = math.log(fixed_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped
    guesses_allowed = max_guesses

    rounds += 1
    guesses_left = guesses_allowed
    secret = random.randint(minimum, maximum)
    print(f"SPOILER: {secret}")
    print(15 * "\n")
    statement_generator(f"ROUND {rounds}", "▶")
    already_guessed = []

    guess = ""
    while guess != secret and guesses_left >= 0:
        guess = int_check(f"Pick a guess out of {minimum} and {maximum}", minimum, maximum, "xxx")

        if guess in already_guessed:
            print(f"You have already guessed that number, you still keep {guesses_left} guesses")
            continue

        # if guess < minimum or guess > maximum:
        #     print("It is higher or lower than the set boundaries 🛡")
        #     continue

        elif guess < secret:
            result = "low"
            try_again = "higher 🔼"
            already_guessed.append(guess)

        elif guess > secret:
            result = "high"
            try_again = "lower 🔽"
            already_guessed.append(guess)

        else:
            result = "You got it"
            try_again = ""

        if result == "You got it":
            print("\n")
            statement_generator("You won! well done", "!")
            results = "Won"

            break

        else:
            guesses_left -= 1

            if guesses_left <= 0:
                result = "Lost"
                print(f"Sorry, you have run out of guesses 😢 the number was {secret}")
                print()
                break

            else:
                print(f"To {result} try a {try_again} number\nYou have {guesses_left} guesses left")

    all_round_wins.append(f"Round {rounds}: {result}, You used {guesses_allowed -  guesses_left} "
                              f"out of {guesses_allowed} guesses")

    ask_stats = yes_no("Would you like to see your statistics? (This round)")
    if ask_stats == "yes":
        statement_generator("ROUND STATISTICS", "+")
        print(f"Guesses allowed: {guesses_allowed}"
              f" \nGuesses needed: {guesses_allowed - guesses_left + 1}\n")
        input("Press <Enter> to carry on")
    play_again = yes_no("Would you like to play again?")
ask_stats = yes_no("Do you want to see your all round statistics")

if ask_stats == "yes":
    statement_generator("ALL ROUND STATISTICS", "*")
    for items in all_round_wins:
        print(items)
