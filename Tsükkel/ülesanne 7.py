"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:

X O O O O O O O X
O X O O O O O X O
O O X O O O X O O
O O O X O X O O O
O O O O X O O O O
O O O X O X O O O
O O X O O O X O O
O X O O O O O X O
X O O O O O O O X
... või (paarisarvulise N-i puhul):

X O O O O O O O O X
O X O O O O O O X O
O O X O O O O X O O
O O O X O O X O O O
O O O O X X O O O O
O O O O X X O O O O
O O O X O O X O O O
O O X O O O O X O O
O X O O O O O O X O
X O O O O O O O O X
Tühikuid võid lisada vastavalt oma soovile."""


def draw_square(size: int, symbol: str):
    for row in range(size):
        for col in range(size):
            if row == col:
                print(f"x", end=" ")
            else:
                print(f" {symbol}", end="")
        print()


if __name__ == '__main__':
    size = int(input("Kui suurt ruutu soovid?" ))
    draw_square(size, "o")


N = int(input("Sisesta ruudu suurus: "))

for i in range(N):
    for j in range(N):
        if i == j or i + j == N - 1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
