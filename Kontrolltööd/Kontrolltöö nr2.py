"""Lahenda ülesanne (ära unusta docstringe)



Koosta programm telefoniraamatu loomiseks.



1.       Peab saama sisestada nime ja telefoni numbrit

2.       Samal nimel võib olla ainult üks telefoni number

3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime

a.       Kui vastet pole, siis peab võimaldama lisamist

4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.       Lisa funktsioon terve raamatu kuvamiseks"""

import json
import os

FILE_NAME = "phonebook.json"


def load_phonebook():
    """
    Load phonebook data from file.
    Returns dictionary with name as key and phone number as value.
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding='utf-8') as file:
            return json.load(file)
    return {}


def save_phonebook(phonebook):
    """
    Save phonebook dictionary into file.
    """
    with open(FILE_NAME, "w", encoding='utf-8') as file:
        json.dump(phonebook, file)


def add_contact(phonebook, name, number):
    """
    Add a new contact to the phonebook.
    Each name can only have one phone number.
    """
    phonebook[name] = number
    save_phonebook(phonebook)


def find_number(phonebook, name):
    """
    Find phone number by name.
    Returns the number or None.
    """
    return phonebook.get(name)


def find_name(phonebook, number):
    """
    Find name by phone number.
    Returns the name or None.
    """
    for name, num in phonebook.items():
        if num == number:
            return name
    return None


def show_phonebook(phonebook):
    """
    Display all contacts in the phonebook.
    """
    if not phonebook:
        print("Telefoniraamat on tühi")
    else:
        for name, number in phonebook.items():
            print(name, "-", number)


def main():
    """
     Main program loop for phonebook management.
    """
    phonebook = load_phonebook()

    while True:
        print("\n1 Lisa kontakt")
        print("2 Otsi tel. number nime järgi")
        print("3 Otsi nimi tel. numbri järgi")
        print("4 Ava telefoniraamat")
        print("5 Lahku")

        choice = input("Vali: ")

        if choice == "1":
            name = input("Nimi: ")
            number = input("Tel. number: ")
            add_contact(phonebook, name, number)

        elif choice == "2":
            name = input("Nimi: ")
            number = find_number(phonebook, name)

            if number:
                print("Number:", number)
            else:
                add = input("Ei leidnud, Kas lisan uue kontakti? (y/n): ")
                if add.lower() == "y":
                    number = input("Tel. number: ")
                    add_contact(phonebook, name, number)


        elif choice == "3":
            number = input("Tel. number: ")
            name = find_name(phonebook, number)

            if name:
                print("Nimi:", name)
            else:
                add = input("Ei leidnud, Kas lisan uue kontakti? (y/n): ")
                if add.lower() == "y":
                    name = input("Nimi: ")
                    add_contact(phonebook, name, number)



if __name__ == '__main__':
    main()