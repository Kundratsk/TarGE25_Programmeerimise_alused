"""Ül 1.
Küsi kasutajalt 3 arvu
Väikseim arv korruta kahega
Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
Teata kas kasutaja vastas õigesti või valesti
Programmi lõpus näita kasutaja valesti vastatud ruutude õiged tulemused (Järjend)
"""





"""
Ül 2.
Küsi kasutaja nime ja vanust
Kui vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
Muidu küsi koosta nime pikkuse jagu arvutus tehteid juhuarvudega (Järjend)
Kuva tehteid ja lase kasutajal vastata, teata kas said õige tulemuse.
Programmi lõpus õnnitle kasutajat erineva tekstiga olenevalt programmi käigust
"""
"""
Ül 3.
Küsi kasutaja vanust ja nime
Õnnitle kasutajat iga täisealisena veedetud aasta eest (Kordus)
Iga õnnitluse järel küsi ja salvest antud aasta meeleolu (Järjend)
Programmi lõpus kuva meeleolud nende pikkuse järjekorras
"""
"""
Ül 4.
Küsi kasutaja sugu ja vanus
Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
Salvesta järjendisse iga kolmas tervitus ja viimane
Kuva ekraanile järjendis olevate tervituste eelviimased sõnad
"""
"""
Ül 5
Küsi kasutajalt lause
Kui lauses on vähem kui 5 sõna, jäta lause meelde ja küsi uus lause (Kordus, Järjend)
Kuva pikas lauses (5 või rohkem sõna) olevad sõnad eraldi real
"""
"""
Ül 6
Kasutajalt küsitakse sõna.
Kasutajalt küsitakse numbrit.
Loo järjend, kus antud sõna on korrutatud kasvavalt kuni antud numbrini (kordus, järjend).
Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
Kuva järjendi viimane väärtus
"""
"""
Ül 7
Küsi kasutajalt 1 arv mille paned astmele 2, 3 ,4 ja 5 kasutades kordust ja järjendit
Lase kasutajal arvata, millises astmes on suvaline arv järjendis
Teata kas arvati õigesti ja kuva õige vastus
Peale seda küsi kasutajalt kas ta soovib teise arvuga programmi korrata või lõpetada. (Kordus)
"""
"""
Ül 8
Küsi kasutajalt arvu.
Kui arv on positiivne, ütle kasutajale, et ta prooviks pigem negatiivset arvu sisestada.
Kui arv on negatiivne, ütle kasutajale, et ta prooviks pigem positiivset arvu sisestada.
Kui arv on 0, õnnitlege kasutajat ja öelge, et olete mängule ära teinud ja pääsete igavesest kordusest.
Kuva ekraanile kasutaja sisestatud arvud kahanevas järjekorras (Järjend)
"""

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

        elif choice == "4":
            show_phonebook(phonebook)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()