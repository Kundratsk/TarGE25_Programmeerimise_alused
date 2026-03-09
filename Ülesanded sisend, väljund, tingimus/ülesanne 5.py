"""Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja
 väljastab tulemuse Fahrenheiti kraadides.
 Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi. """


def convert_to_fahrenheit(celsius_temperature: float) -> float:
    return celsius_temperature * 1.8 + 32


def convert_to_celsius(fahrenheit_temperature: float) -> float:
    return (fahrenheit_temperature - 32) / 1.8


if __name__ == "__main__":
    unit = input("Määra sisestatava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuur Celsius kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_fahrenheit: .2F}F kraadi. ")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur Fahrenheit kraadides: "))
        temperature_celsius = convert_to_celsius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit}F on {temperature_celsius: .2F}C kraadi. ")
    else:
        print(f"Sisestasid tundmatu temperatuuri ühiku - {unit}")
        print("Programm toetab C - Celsius ja F - Fahrenheit kraade")