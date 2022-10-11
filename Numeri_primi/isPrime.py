import math

fattori_primi = []

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True

def fattPrime(num):
    divisori = []
    for i in fattori_primi:
        if(num % i == 0):
                divisori.append(i)

    return divisori


def main():
    num = -1

    f = open("./numeri_primi.txt", "r")
    righe = f.readlines()

    for riga in righe:
        fattori_primi.append(int(riga))

    while(num <= 1):
        num = int(input("inserisci un numero: "))

    print(f"Divisori primi: {fattPrime(num)}")

"""
    if(isPrime(num)):
        print("il numero è primo")
    else:
        print("il numero non è primo")
"""

if __name__ == "__main__":
    main()