"""Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos
 vastusega. Näiteks:
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5
"""
from unittest import result


def calculator(num1: float, num2: float, operation: str) -> str:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "**":
        result = num1 ** num2

    if result == "":
        return f"tundmatu tehe: {operation}"
    return f"{num1}{operation}{num2}={result}"


if __name__ == '__main__':
    num1 = float(input("Sisestage esimene arv: "))
    num2 = float(input("Sisestage teine arv: "))
    operation = input("Sisestage tehtemärk: ")
    print(F"Tulemus: {calculator(num1, num2, operation)}")