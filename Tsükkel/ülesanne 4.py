from random import randint

# arvuti mõtleb arvu
secret_number = randint(1, 20)
attempts = 0
max_attempts = 5

print("Mõtlesin ühele täisarvule 1–20ni. Mis arv see on?")


while attempts < max_attempts:
    guess = int(input(">> "))
    attempts += 1
    if guess > secret_number:
        print("Liiga suur, proovi uuesti.")
    elif guess < secret_number:
        print("Liiga väike, proovi uuesti.")
    else:
        print(f"Tubli, arvasid ära. Arv oli {secret_number}.")
        break
else:
    print(f"Katsed said otsa! Õige arv oli {secret_number}.")