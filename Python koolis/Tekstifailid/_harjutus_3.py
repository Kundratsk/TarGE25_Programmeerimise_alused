"""Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon)."""

from _harjutus_2 import write_poem_file


def get_row_number():
    line_number = int(input(f"Mitmendat rida soovid kuvada? :"))
    with open("poem.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        if line_number > 0:
            wanted_line = lines[line_number - 1].strip()
            print(wanted_line)
        elif line_number > 8 or line_number < 1:
            print("Rida ei ole olemas")




if __name__ == '__main__':
    get_row_number()