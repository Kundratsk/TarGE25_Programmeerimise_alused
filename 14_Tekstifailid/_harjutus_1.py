"""Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale, perekonna- ja
 eesnimi tühikuga eraldatult). Koosta programm, mis loeb failist andmed ja väljastab need ekraanile tähestikulises
 järjekorras. Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi (järjestamist). Tähestikulises
 järjekorras salvestage tuttavate nimed ka uude faili tuttavad1.txt.
"""


def create_familiars_file(filename: str):

    familiars = [
        "Tiit Sukk",
        "Teet Pukk",
        "Peep Nukk",
        "Tina Kukk",
        "Mari Tukk",
        "Sari Lupp"
    ]
    with open("tuttavad.txt", "w", encoding="utf-8") as f:
        for name in familiars:
            f.write(name + "\n")


def read_names_from(filename: str) -> list[str]:
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if len(name) > 0:
                result.append(name)
    return result


def sort_names(names):
    last_name__full_name_list = []
    for name in names:
        last_name = name.split()[-1]
        last_name__full_name_list += [(last_name, name)]

    sorted_names = sorted(last_name__full_name_list)
    result = []
    for name in sorted_names:
        result_name = name[-1]
        result.append(result_name)
    return result


if __name__ == '__main__':
    filename = "tuttavad.txt"
    create_familiars_file(filename)
    names_from_file = read_names_from(filename)
    sorted_by_last_name = sort_names(names_from_file)
    for name in sorted_by_last_name:
        print(name)


