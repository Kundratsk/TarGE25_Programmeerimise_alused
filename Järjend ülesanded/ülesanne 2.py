"""Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv
leitakse vastava funktsiooni abil."""

capitals = ["Tallinn", "Riia", "Tirana", "Helsinki","Rooma", "Belgrad", "Vilnius", "Sofia", "Oslo", "Stockholm" ]
def print_list(elements: list) -> None:
    for element in elements:
        print(element, end=", ")
    print()


def sort_in_place(elements: list) -> None:
    elements.sort()


def add_capitals(capitals: list[str], amount: int) -> None:
    for i in range(amount):
        capitals.append(input(f"{i + 1}. Sisesta euroopa pealinn:"))


def print_list_numbered(elements: list):
    for index, element in enumerate(elements):
        print(f"{index + 1}. {element}")

def summarize(capitals: list[str]) -> None:
    print(f"Meie järjendis on {len(capitals)} Euroopa pealinna")


if __name__ == '__main__':
    print_list(capitals)
    sort_in_place(capitals)
    print_list(capitals)
    add_capitals(capitals, 2)
    sort_in_place(capitals)
    print_list(capitals)
    print_list_numbered(capitals)
    summarize(capitals)