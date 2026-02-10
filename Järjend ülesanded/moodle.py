from ctypes import HRESULT


def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    result = " "
    while count > 0:
        result += "hola"
        count -= 1

if __name__ == '__main__':
    make_hola_string(3)
    make_hola_string(0)


import random
def generate_string_with_random_length(threshold: float) -> str:
    result = " "

    while random.random() < threshold:
        result += "-"

    return result

"""Kirjuta funktsioon, mis küsib kasutajalt tema vanust (What is your age?).
Funktsioonile antakse ette alumine vanuspiir. Kasutaja peab sisestama
vanuse, mis on suurem-võrdne sellest vanusepiirist ning väiksem-võrdne
100-ga. Kui kasutaja ei sisesta sobivat vanust, prinditakse välja
hoiatus ning küsitakse vanust uuesti."""

def ask_user_age(age_limit: int) -> int:
    while True:
        age_input = input("What is your age? ")
        if not age_input.isdigit():
            print(f"Wrong input!")
            continue

        age = int(age_input)
        if age > 100:
            print("Too old!")
        else:
            print("Too young!")

        return age

""""Koosta vähemalt kümnest elemendist koosnev järjend arvudest. Koosta programm, mis küsib kasutajalt tegurit ja 
korrutab kõik algses järjendis olnud arvud sellega läbi ning väljastab tulemuse ekraanile.
Sisesta tegur: 3
45 * 3 = 135
7 * 3 = 21
...
267 * 3 = 801"""

from random import randint

def generate_number_list(smallest: int, largest: int) -> list[int]:
    result = []
    for i in range (10):
        random_number = randint(smallest, largest)
        result.append(random_number)
    return result

def ask_user_int(question: str) -> int:
    user_input = input(question)
    while not user_input.isdigit():
        print("Input not an integer, Please try again.")
        user_input = input(question)
    return int(user_input)

def multiply_list(numbers: list[int], multiplier: int) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * multiplier)
    return result

def show_result(original_numbers: list[int], multiplier: int, resulting_numbers: list[int]) -> None:
    for i in range (len(original_numbers)):
        print(f"{original_numbers[i]} x {multiplier} = {resulting_numbers[i]}")

if __name__ == '__main__':
    numbers_list = generate_number_list(1, 10)
    multiplier = ask_user_int("Please insert multiplier: ")
    multiplied_list = multiply_list(numbers_list, multiplier)
    show_result(numbers_list, multiplier, multiplied_list)









