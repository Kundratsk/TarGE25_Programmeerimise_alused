""""Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta
ei ole midagi teada. Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse
iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on
vaja programmi, mis arvutab"""
from threading import main_thread


def calculate_budget(guests: int) -> int:

    venue_price = 55
    price_per_guest = 10
    return venue_price + price_per_guest * guests


if __name__ == '__main__':
    invited_guests = int(input("Mitu inimest on peole kutsutud? "))
    confirmed_guests = int(input("Mitu inimest juba tuleb? "))
    min_budget = calculate_budget(confirmed_guests)
    max_budget = calculate_budget(invited_guests)
    print(f"Maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")