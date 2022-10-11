import random

lettere = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'l': 9, 'm': 10, 'n': 11, 'o': 12, 'p': 13, 'q': 14, 'r': 15, 's': 16, 't': 17, 'u': 18, 'v': 19, 'z': 20}
lett_inv = {v: k for k, v in lettere.items()}

def generaChiave(parola):
    chiave = ""

    for i in range(len(parola)):
        chiave += lett_inv[random.randint(0,20)]

    #return chiave
    return "itis"

def conversione(lista_crip, dictLett):
    print(dictLett)
    print(lista_crip)
    cript = ""
    for elem in lista_crip:
        for lett in dictLett:
            if(dictLett[lett] == elem):
                cript = cript + lett
            elif(lett == elem):
                cript = cript + lett_inv[lett]

    return cript

def criptazione():
    parola = input("Inserisci parola da codificare: ")
    lista_parola = [lettere[elem] for elem in parola]

    chiave = generaChiave(parola)
    lista_chiave = [lettere[elem] for elem in chiave]

    lista_crip = [(lista_chiave[i]+lista_parola[i])%len(lettere) for i in range(len(parola))]

    return conversione(lista_crip, lettere)

def decriptazione():
    parola = input("Inserisci parola da decodificare: ")
    lista_parola = [lettere[elem] for elem in parola]

    chiave = generaChiave(parola)
    lista_chiave = [lettere[elem] for elem in chiave]

    lista_crip = [(lista_parola[i]-lista_chiave[i])%len(lettere) for i in range(len(parola))]

    return conversione(lista_crip, lett_inv)

def main():
    #print(criptazione())
    print(decriptazione())
    #print(generaChiave("ciao"))

if __name__ == "__main__":
    main()