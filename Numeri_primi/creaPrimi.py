import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True

def main():
    f = open("./numeri_primi.txt", "w")

    for i in range(2,10000000):
        if(isPrime(i)):
            f.write(str(i) + "\n")

    f.close()

if __name__ == "__main__":
    main()