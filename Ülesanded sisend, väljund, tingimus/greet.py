"""Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos tekstiga,
mis ütleb, kas tegemist on 7-18-aastase inimesega. """


def greet_in_name(name: str) -> str:
    return f"Tervist {name}!"


def verify_age(age: int) -> str:
    if 7 <= age <= 18:
        return "Oled 7-18 Aastane"
    return "Oled noorem kui 7 aastane või vanem kui 18 aastane"

if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus aastates täisarvuna: "))
    greeting = greet_in_name(name)
    age_text = verify_age(age)
    print(greeting, age_text)



