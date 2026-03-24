"""
Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt uut rida lisada ning seejärel
lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
"""

from _harjutus_2 import write_poem_file


if __name__ == '__main__':
    file_name = "poem.txt"
    write_poem_file(file_name)
    poem_line = input("Sisesta rida, mille järele soovid uut rida lisada:")


    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    found = False
    for i in range(len(lines)):
        if lines[i].strip() == poem_line:
            found = True
            position = i
            break

    if not found:
        print("Antud rida ei leitud failist.")
    else:
        line_to_append = input("Sisesta rida, mida sooovid lisada:")
        lines.insert(position + 1, line_to_append + "\n")

        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("Rida lisatud edukalt!")
