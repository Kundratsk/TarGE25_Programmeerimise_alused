"""1. Küsi kasutaja sugu ja vanus
2. Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3. Korda tervitust ea suurendamisega kuni tervitus vahetub või 10 korda."""


def tervitus(sugu, vanus):
    nimetus = "Härra" if sugu == "m" else "Proua"


    if vanus < 18:
        return f"Tere, {nimetus}"
    elif vanus < 65:
        return f"Lugupidamisega, {nimetus}"
    else:
        return f"Lugupidamise ja austusega, {nimetus}"


def main():
    sugu = input("Sisesta sugu (m/n): ").lower()
    vanus = int(input("Sisesta vanus: "))

    eelmine = tervitus(sugu, vanus)

    for i in range(10):
        praegune = tervitus(sugu, vanus)

        if praegune != eelmine:
            break

        print(f"{praegune} ({vanus} a.)")
        vanus += 1


if __name__ == "__main__":
    main()


