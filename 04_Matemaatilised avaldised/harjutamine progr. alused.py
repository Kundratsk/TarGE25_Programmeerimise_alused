def kusi_kolm_arvu():
    arvud = []
    for i in range(3):
        arv = int(input(f"Sisesta arv {i+1}: "))
        arvud.append(arv)
    return arvud


def kontrolli_ruute(piir):
    valed_vastused = []

    for i in range(1, piir + 1):
        kasutaja_vastus = int(input(f"Mis on arvu {i} ruut? "))
        oige_vastus = i ** 2

        if kasutaja_vastus == oige_vastus:
            print("Õige!\n")
        else:
            print("Vale!\n")
            valed_vastused.append((i, oige_vastus))

    return valed_vastused


def main():

    arvud = kusi_kolm_arvu()


    vaikseim = min(arvud)
    piir = vaikseim * 2
    print(f"\nVäikseim arv on {vaikseim}, korrutatuna kahega: {piir}\n")


    valed_vastused = kontrolli_ruute(piir)


    print("Valesti vastatud ruudud:")
    if valed_vastused:
        for arv, ruut in valed_vastused:
            print(f"{arv}² = {ruut}")
    else:
        print("Kõik vastused olid õiged!")



if __name__ == "__main__":
    main()

"""ÜL 2"""

import random


# ---------- ÜL 2 ----------
def ul2():
    nimi = input("Sisesta nimi: ")
    vanus = int(input("Sisesta vanus: "))

    if vanus < 5:
        for _ in range(3):
            print(f"Tere, {nimi}!")
        print("Sa oled veel väga noor 😊")
    else:
        tehteid = []
        vastused_oiged = 0

        for _ in range(len(nimi)):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            tehteid.append((a, b))

        for a, b in tehteid:
            vastus = int(input(f"{a} + {b} = "))
            if vastus == a + b:
                print("Õige!")
                vastused_oiged += 1
            else:
                print("Vale!")

        if vastused_oiged == len(tehteid):
            print("Tubli! Kõik vastused olid õiged 🎉")
        else:
            print("Hea töö, harjutamine teeb meistriks 🙂")

"""ÜL 3"""

def ul3():
    nimi = input("Sisesta nimi: ")
    vanus = int(input("Sisesta vanus: "))

    meeleolud = []

    for aasta in range(18, vanus + 1):
        print(f"Õnnitleme {nimi}, oled olnud täisealine {aasta - 17} aastat!")
        meeleolu = input("Milline oli selle aasta meeleolu? ")
        meeleolud.append(meeleolu)

    meeleolud.sort(key=len)

    print("\nMeeleolud pikkuse järjekorras:")
    for m in meeleolud:
        print(m)

"""ÜL 4"""

def ul4():
    sugu = input("Sisesta sugu (mees/naine): ").lower()
    vanus = int(input("Sisesta vanus: "))

    tervitused = []
    kordused = 0

    while kordused < 10:
        if sugu == "mees":
            if vanus < 18:
                tervitus = f"Tere poiss, vanus {vanus}"
            else:
                tervitus = f"Tere härra, vanus {vanus}"
        else:
            if vanus < 18:
                tervitus = f"Tere tüdruk, vanus {vanus}"
            else:
                tervitus = f"Tere proua, vanus {vanus}"

        print(tervitus)

        if kordused % 3 == 2:
            tervitused.append(tervitus)

        kordused += 1
        vanus += 1

    tervitused.append(tervitus)

    print("\nSalvestatud tervituste eelviimased sõnad:")
    for t in tervitused:
        print(t.split()[-2])

"""ÜL 5"""

def ul5():
    luhikesed = []

    while True:
        lause = input("Sisesta lause: ")
        sonad = lause.split()

        if len(sonad) < 5:
            luhikesed.append(lause)
        else:
            print("\nPika lause sõnad:")
            for s in sonad:
                print(s)
            break
"""ÜL 6"""

def ul6():
    sona = input("Sisesta sõna: ")
    number = int(input("Sisesta number: "))

    if number > 10:
        print("Viga")
        return

    jarjend = []
    for i in range(1, number + 1):
        jarjend.append(sona * i)

    print("Järjendi viimane väärtus:", jarjend[-1])

"""ÜL 7"""

def ul7():
    while True:
        arv = int(input("Sisesta arv: "))

        # 1. Astmed 2–5 (kordus + järjend)
        astmed = []
        for aste in range(2, 6):
            astmed.append(arv ** aste)

        # 2. Suvaline arv järjendist
        indeks = random.randint(0, len(astmed) - 1)
        suvaline_arv = astmed[indeks]

        print("\nMillises astmes (2–5) on järgmine arv?")
        print(suvaline_arv)

        pakkumine = int(input("Sinu vastus (aste): "))

        # 3. Kontroll
        oige_aste = indeks + 2
        if pakkumine == oige_aste:
            print("Õige vastus! 🎉")
        else:
            print(f"Vale vastus. Õige aste oli {oige_aste}.")

        # 4. Kordamine või lõpetamine
        uuesti = input("\nKas soovid uue arvuga jätkata? (jah/ei): ").lower()
        if uuesti != "jah":
            break

""" ÜL 8"""

def ul8():
    sisestatud_arvud = []

    while True:
        arv = int(input("Sisesta arv: "))
        sisestatud_arvud.append(arv)

        if arv > 0:
            print("Proovi pigem negatiivset arvu.")
        elif arv < 0:
            print("Proovi pigem positiivset arvu.")
        else:
            print("Õnnitleme! Oled mängu ära teinud ja pääsed igavesest kordusest 🎉")
            break

    # 5. Kahanev järjekord
    sisestatud_arvud.sort(reverse=True)

    print("\nSisestatud arvud kahanevas järjekorras:")
    for a in sisestatud_arvud:
        print(a)
