"""Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri ja iga rea järele
sulgudesse reas asuvate sümbolite arvu e. rea pikkuse."""


def write_poem_file(filename :str):
    with open("poem.txt", "w", encoding="utf-8") as f:
        f.write("""Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.""")

def add_row_number_to_poem():
    with open("poem.txt", "r", encoding="utf-8") as f:
        rows = f.readlines()

    for index, row in enumerate (rows, start=1):
        clean = row.strip("\n")
        length = len(clean)
        print(f"{index}.  {clean} ({length})")


if __name__ == '__main__':
    filename = "poem.txt"
    add_row_number_to_poem()

