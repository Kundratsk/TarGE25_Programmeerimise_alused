"""On selge, et auto kiiruse tõstmine vähendab sõidule kuluvat aega ehk ma jõuame varem sihtpunkti. Kui palju
me aga ajas võidame? Koostage programm, mis küsib käivitamisel läbitava vahemaa pikkust (kilomeetrites, see
kehtib kogu programmitöö aja), seejärel aga küsib kasutajalt korduvalt kiirust (km/h) ning väljastab selle
põhjal korrektse lausega sõiduks kuluva aja ja erinevuse eelmisest tulemusest. Kui kasutaja uut kiirust ei
sisesta, vaid vajutab lihtsalt sisestusklahvile, siis katkestatakse tsükkel ja tänatakse kasutajat."""


distance = float(input("Sisesta läbitav vahemaa (km): "))

previous_time = None

while True:
    speed_input = input("Sisesta kiirus (km/h), või vajuta Enter lõpetamiseks: ")


    if speed_input == "":
        print("Aitäh! Programm lõpetatud.")
        break


    speed = float(speed_input)


    current_time = distance / speed


    print(f"Aeg sõiduks: {current_time:.2f} tundi")


    if previous_time is not None:
        difference = previous_time - current_time
        print(f"Aja erinevus eelmisest kiirusest: {difference:.2f} tundi")


    previous_time = current_time



