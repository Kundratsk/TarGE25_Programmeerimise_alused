""" Write a function (numbers_game) that doesn’t take any arguments.
When we run it, the function chooses a random integer between 0 and 100 (100 included).
Then we ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates the following:
Too high, Too low, or Correct!
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly."""

import random


def numbers_game():


    number = random.randint(0,15)
    guesses = 3

    while guesses > 0:
        guess = int(input("Arva ära mu number: "))

        if guess == number:
            print("Arvasid ära!")
            break
        elif guess < number:
            guesses -= 1
            print("Liiga väike, proovi uuesti!")
        else:
            guesses -= 1
            print("Liiga suur, proovi uuesti ")

        print(f"Sul on alles {guesses} katset ")

    if guesses == 0:
        print(f"Mäng läbi! Õige number oli {number}")

if __name__ == '__main__':
    numbers_game()





