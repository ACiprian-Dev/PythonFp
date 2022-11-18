from validare.validare_numere import valideaza_numar, valideaza_pozitie, valideaza_interval


def convertCalculationsListToDisplayList(calculationsList):
    '''
    Transforma lista de numere complexe folosite pentru calcule intr-o lista de numere complexe pentru afisare
    :param calculationsList: lista de numere complexe folosite pentru calcule
    :return: returneaza o lista de numere complexe folosite pentru afisare
    '''

    displayList = []

    for i in range(getLengthOfList(calculationsList)):
        if calculationsList[i].real == 0 and calculationsList[i].imag == 0:
            displayList.append(f"{calculationsList[i].real}")
        elif calculationsList[i].real == 0:
            displayList.append(f'{calculationsList[i].imag}i')
        elif (calculationsList[i].imag == 0):
            displayList.append(f'{calculationsList[i].real}')
        else:
            displayList.append(f'{calculationsList[i].real} + {calculationsList[i].imag}i')

    return displayList

def convertCalculationToDisplay(number):
    '''
    Transforma un numar complex folosit pentru calcule intr-un numar complex folosit pentru afisare
    :param number: un numar complex
    :return: un numar complex folosit pentru afisare
    '''
    if number.real == 0 and number.imag == 0:
        return f"{number.real}"
    elif number.real == 0:
        return f"{number.imag}i"
    elif number.imag == 0:
        return f"{number.real}"
    else:
        return f"{number.real} + {number.imag}i"

def addComplexNumberToList(l, complexNumber):
    '''
    adauga un numar complex dat de forma a + bi la lista l
    :param l: lista actuala de numere complexe
    :param a: partea reala a numarului complex ce trebuie adaugat
    :param b: partea imaginara a numarului complex ce trebuie adaugat
    :return: -
    '''

    l.append(complexNumber)


def addComplexNumberAtPosition(l, complexNumber, poz):
    '''
    adauga un numar complex de form a + bi in lista l pe pozitia poz
    :param l: lista actuala de numere complexe
    :param a: partea reala a numarului complex ce trebuie adaugat
    :param b: partea imaginara a numarului complex ce trebuie adaugat
    :param poz: pozitia in care trebuie inserat numarul complex
    :return: -
    '''



    l.insert(poz, complexNumber)

def getLengthOfList(l):
    '''
    calculeaza lungimea listei l
    :param l: lista de numere complexe
    :return: un numar intreg
    '''
    return len(l)

def removeComplexNumberAtPosition(l, poz):
    '''
    Sterge numarul complex de pe pozitia poz (numar intreg) din lista l
    :param l: lista de numere complexe
    :param poz: numar intreg
    :return: -
    '''
    poz = int(poz)

    while True:
        if(getLengthOfList(l)==0):
            print("Lista dumneavoastra este goala")
        elif(poz>getLengthOfList(l)):
            print("Nu exista pozitia data in lista dumneavoastra")
            poz = int(input("poz = "))
        else:
            break

    del l[poz]

def removeComplexNumbersInInterval(l, startInterval, endInterval):
    '''
    Sterge o subsecventa de numere complexe din lista l
    :param l: lista de numere complexe
    :param startInterval: pozitia de start pentru subsecventa
    :param endInterval: pozitia de final pentru subsecventa
    :return: -
    '''
    del l[startInterval:endInterval+1]

def replaceAllOccurrencesOfComplexNumber(l, replacement, numberToReplace):
    '''
    Inlocuieste toate aparitiile parametrului numberToReplace din lista l cu parametrul replacement
    :param l: lista de numere complexe
    :param replacement: numar complex
    :param numberToReplace: numar complex
    :return: -
    '''
    replacement = replacement
    numberToReplace = numberToReplace

    for i in range(getLengthOfList(l)):
        if(l[i] == numberToReplace):
            l[i] = replacement

def getImaginaryPartOfNumbers(l, startInterval, endInterval):
    '''
    Returneaza o lista newList alcatuita din partea imaginara a numerelor complexe din lista l din subsecventa definita de intervalul delimitat de startInterval si endInterval
    :param l: lista de numere complexe
    :param startInterval: numar intreg
    :param endInterval: numar intreg
    :return: lista newList
    '''

    newList = []
    for i in range(startInterval, endInterval + 1, 1):
        newList.append(l[i].imag)
    return newList



def getModulusOfComplexNumber(complexNumber):
    '''
    Returneaza modulul unui numar complex complexNumber
    :param complexNumber: numar complex
    :return: float
    '''
    return abs(complexNumber)

def getListOfNumbersWithModulusLessThan10(l):
    '''
    Returneaza o lista de numere complexe cu modulul mai mic decat 10
    :param l: lista de numere complex
    :return: lista de numere complexe
    '''
    newList = []
    for i in range(getLengthOfList(l)):
        if(getModulusOfComplexNumber(l[i]) < 10):
            newList.append(l[i])

    return newList

def getListOfNumbersWithModulus10(l):
    '''
    Returneaza o lista de numere complexe cu modulul 10
    :param l: lista de numere complexe
    :return: lista de numere complexe
    '''
    newList = []
    for i in range(getLengthOfList(l)):
        if(getModulusOfComplexNumber(l[i])==10):
            newList.append(l[i])
    return newList

def getSumOfNumbersInInterval(l, startInterval, endInterval):
    '''
    Returneaza suma(numar complex) numerelor complexe din lista l din intervalul [startInterval:endInterval]
    :param l: lista de numere complex
    :param startInterval: numar intreg
    :param endInterval: numar intreg
    :return: numar complex
    '''
    suma = 0
    for i in range(startInterval, endInterval + 1, 1):
        suma += l[i]

    return suma

def getProductOfNumbersInInterval(l, startInterval, endInterval):
    '''
    Returneaza produsul(numar complex) numerelor complexe din lista l din intervalul [startInterval:endInterval]
    :param l: lista de numere complexe
    :param startInterval: numar intreg
    :param endInterval: numar intreg
    :return: numar complex
    '''
    prod = 1
    for i in range(startInterval, endInterval + 1, 1):
        prod *= l[i]

    return prod

def getImaginary(complexNumber):
    '''
    Returneaza partea imaginara a unui numar complex
    :param complexNumber: numar complex
    :return: float
    '''
    return complexNumber.imag

def createNewListWithSameValues(l):
    '''
    Creaza o lista noua independeta cu aceleasi valori ca lista l
    :param l: lista de numere complexe
    :return: lista de numere complexe
    '''
    newList = []
    for i in range(getLengthOfList(l)):
        newList.append(l[i])

    return newList

def reverseSortByImaginary(l):
    '''
    Sorteaza descrescator lista l dupa partea imaginara a numerelor complexe din aceasta
    :param l: lista de numere complexe
    :return: lista de numere complexe
    '''
    newList = createNewListWithSameValues(l)
    newList.sort(reverse=True, key=getImaginary)

    return newList

def isNumberPrime(number):
    '''
    Returneaza True daca numarul intreg number este prim si False in caz opus
    :param number: numar intreg
    :return: bool
    '''
    prime = True

    if(number < 2):
        prime = False
    else:
        for i in range(2, int(number/2), 1):
            if number % i == 0:
                prime = False
    return prime

def filterOutPrimeNumbers(l):
    '''
    Elimina toate numerele complexe ce au partea reala numar prim din lista l
    :param l: lista de numere complexe
    :return: -
    '''
    l[:] = [value for value in l if not isNumberPrime(value.real)]

def filterModulusLessThan(l, modulus):
    '''
    Elimina toate numerele complexe din lista l ce au modulul mai mic decat modulus
    :param l: lista de numere complexe
    :param modulus: int or float
    :return: -
    '''
    l[:] = [value for value in l if not getModulusOfComplexNumber(value) < modulus]

def filterModulusGreaterThan(l, modulus):
    '''
    Elimina toate numerele complexe din lista l ce au modulul mai mare decat modulus
    :param l: lista de numere complexe
    :param modulus: int or float
    :return: -
    '''
    l[:] = [value for value in l if not getModulusOfComplexNumber(value) > modulus]

def filterModulusEqual(l, modulus):
    '''
    Elimina toate numerele complexe din lista l ce au modulul egal cu modulus
    :param l: lista de numere complexe
    :param modulus: int or float
    :return: -
    '''
    l[:] = [value for value in l if getModulusOfComplexNumber(value) != modulus]

# def myUndo(lastKnownList):
#     '''
#     Returneaza o lista nou
#     :param lastKnownList:
#     :return:
#     '''
#     list3 = [value for value in lastKnownList]
#     return list3


