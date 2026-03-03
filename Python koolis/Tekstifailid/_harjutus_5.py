"""Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt
 ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne). Loo programm, mis trükib ekraanile välja kõik tekstifailis
 olevad sõnad, mis on palindroomid. Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega
 , kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt"""

import string


def find_palindromes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("Palindromes found in text:")
            print("-" * 25)

            for line in file:
                words = line.split()

                for word in words:
                    clean_word = word.strip(string.punctuation).lower()

                    if len(clean_word) > 1 and clean_word == clean_word[::-1]:
                        print(clean_word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == '__main__':
    find_palindromes("lemmad2013.txt")


