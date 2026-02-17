"""Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles kui morse koodina, lubab
seejärel kasutajal sisestada sõnu ning teisendab need sümbolhaaval morsetähestikku (lisades iga sümboli
järele tühiku). Sõnastik ei pruugi sisaldada kõikvõimalikke märke, seega tuleb iga sümboli puhul kontrollida,
kas see üldse esineb sõnastikus. Tähe registrit ehk suur- ja väiketähti ei eristata. Samuti tuleb otsustada, mida
ette võtta nende tähtedega, mida inglise tähestikus pole (näiteks "õ", "ä" jne): ignoreerida või mõned neist teisendada
(näiteks "õ" -> "o" vms).

Programm võiks küsida kasutajalt sõnu kas mingi arv kordi või töötada lõpmatult, kuni kasutaja sõna ei sisesta, vaid
 vajutab lihtsalt sisestusklahvile."""


tahestik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":
    ".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
    "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "Ö": "---", "Ä": ".-", "Ü": "..-","Õ": "---"}
def name_to_morse(name: str) -> str:
    result = []
    for char in name.upper():
        if char in tahestik:
            result.append(tahestik[char])
    return " ".join(result)


def ask_name_and_greet():
    name = input("Sisesta oma nimi")

    print(f"Tere, {name}!")

    morse_name = name_to_morse(name)

    print(f"Sinu nimi morse koodis: {morse_name}")


if __name__ == '__main__':
    ask_name_and_greet()


