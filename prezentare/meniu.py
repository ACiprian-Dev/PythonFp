from infrastructura.lista_repository import addComplexNumberToList, addComplexNumberAtPosition, \
    removeComplexNumberAtPosition, removeComplexNumbersInInterval, replaceAllOccurrencesOfComplexNumber, \
    convertCalculationsListToDisplayList, getLengthOfList, getImaginaryPartOfNumbers, \
    getListOfNumbersWithModulusLessThan10, getListOfNumbersWithModulus10, getSumOfNumbersInInterval, \
    convertCalculationToDisplay, getProductOfNumbersInInterval, reverseSortByImaginary, filterOutPrimeNumbers, \
    filterModulusLessThan, filterModulusGreaterThan, filterModulusEqual, createNewListWithSameValues
from validare.validare_numere import valideaza_numar, valideaza_pozitie, valideaza_numar_de_inlocuit, valideaza_interval


def printCurrentList(l):
    print("Lista dumneavoastra de numere complexe este urmatoarea:")
    print(l)


def printMenu():
    print("Alegeti ce operatiune doriti sa faceti:")
    print("     + pentru a adauga un numar complex in lista")
    print("     - pentru a modifica elementele din lista")
    print("     ? pentru a efectua operatii de cautare asupra numerelor din lista")
    print("     * pentru a efectua operatii asupra numerelor din lista")
    print("     / pentru a filtra elementele din lista")
    print("     u pentru a efectua o operatie de undo")
    print("     x pentru a iesi din aplicatie")


def printMenuAdaugare():
    print("Alegeti ce fel de adaugare doriti sa faceti:")
    print("     1 pentru a adauga un numar complex la sfarsitul listei")
    print("     2 pentru a insera un numar complex pe ce pozitie doriti")
    print("     x pentru a va intoarce in meniul principal")


def adaugaNumarComplex(calculationsList):
    print("Numarul vostru este de forma a + bi, specificati valorile pentru a si b")
    a = input("a = ")
    a = valideaza_numar(a, "a")
    b = input("b = ")
    b = valideaza_numar(b, "b")

    addComplexNumberToList(calculationsList, complex(a,b))



def adaugaNumarComplexPePozitie(l):
    print(f"Numarul vostru este de forma a + bi, specificati valorile pentru a si b si pozitia pe care doriti sa inserati numarul, iar lungimea actuala a listei este {len(l)}")
    a = input("a = ")
    a = valideaza_numar(a, "a")
    b = input("b = ")
    b = valideaza_numar(b, "b")
    poz = input("pozitia = ")
    poz = valideaza_pozitie(poz, "pozitie")

    addComplexNumberAtPosition(l, complex(a, b),poz)



def menuAdaugare(calculationsList):
    printMenuAdaugare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        adaugaNumarComplex(calculationsList)
    elif(n=='2'):
        adaugaNumarComplexPePozitie(calculationsList)


def printMenuModificare():
    print("Alegeti ce fel de modificare doriti sa faceti:")
    print("     1 pentru a sterge un numar complex de pe o pozitie data")
    print("     2 pentru a sterge numerele complexe de pe un interval dat")
    print("     3 pentru a inlocui toate aparitiile unui numar complex cu alt numar complex")
    print("     x pentru a va intoarce in meniul principal")


def stergeNumarComplexPePozitie(l):
    print("Specificati pozitia de pe care doriti sa stergeti numarul complex")
    poz = input("poz = ")
    poz = valideaza_pozitie(poz, "pozitie")
    removeComplexNumberAtPosition(l,poz)


def stergeNumereComplexePeInterval(l):
    print("Specificati pe ce interval doriti sa stergeti elemente din lista")
    startInterval = input("start interval = ")
    endInterval = input("sfarsit interval = ")
    startInterval = valideaza_pozitie(startInterval, "start interval")
    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
    lengthOfList = getLengthOfList(l)

    startInterval, endInterval = valideaza_interval(lengthOfList, startInterval, endInterval)

    removeComplexNumbersInInterval(l, startInterval, endInterval)


def inlocuiesteToateAparitiileUnuiNumarComplex(l):
    print("Specificati ce numar complex doriti sa inlocuiti")
    a = input("Partea reala a numarului de inlocuit = ")
    a = valideaza_numar(a, "a")
    b = input("Partea imaginara a numarului de inlocuit = ")
    b = valideaza_numar(b, "b")
    numberToReplace = complex(a, b)
    numberToReplace = valideaza_numar_de_inlocuit(l, numberToReplace)

    print("Specificati cu ce numar complex ati dori sa inlocuiti acest numar")
    a = input("Partea reala a inlocuitorului = ")
    a = valideaza_numar(a, "a")
    b = input("Partea imaginara a inlocuitorului = ")
    b = valideaza_numar(b, "b")
    replacement = complex(a, b)


    replaceAllOccurrencesOfComplexNumber(l, replacement, numberToReplace)



def menuModificare(l):
    printMenuModificare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        stergeNumarComplexPePozitie(l)
    elif(n=='2'):
        stergeNumereComplexePeInterval(l)
    elif(n=='3'):
        inlocuiesteToateAparitiileUnuiNumarComplex(l)


def printMenuCautare():
    print("Alegeti ce fel de cautare doriti sa faceti:")
    print("     1 pentru a tipari partea imaginara a numerelor din lista de pe intervalul specificat de dumneavoastra")
    print("     2 pentru a tipari toate numerele complexe care au modulul mai mic decat 10")
    print("     3 pentru a tipari toate numerele complexe care au modulul egal cu 10")
    print("     x pentru a va intoarce in meniul principal")


def tiparesteParteaImaginara(l):
    print("Specificati pe ce interval din lista doriti sa tipariti partea imaginara")
    startInterval = input("start interval = ")
    endInterval = input("sfarsit interval = ")
    startInterval = valideaza_pozitie(startInterval, "start interval")
    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
    lengthOfList = getLengthOfList(l)

    startInterval, endInterval = valideaza_interval(lengthOfList, startInterval, endInterval)

    newList = getImaginaryPartOfNumbers(l, startInterval, endInterval)
    print("Lista cu partea imaginara a numerelor din secventa dumneavoastra este urmatoarea:")
    print(newList)


def tiparesteNumereleCuModulSub10(l):

    newList = getListOfNumbersWithModulusLessThan10(l)
    if(newList):
        newList = convertCalculationsListToDisplayList(newList)
        print("Lista cu numerele complexe cu modul sub 10 din lista dumneavoastra este urmatoarea:")
        print(newList)
    else:
        print("Nu exista numere complexe cu modul sub 10 in lista dumneavoastra")


def tiparesteNumereleCuModul10(l):
    newList = getListOfNumbersWithModulus10(l)
    if(newList):
        newList = convertCalculationsListToDisplayList(newList)
        print("Lista cu numerele complexe cu modul 10 din lista dumneavoastra este urmatoarea:")
        print(newList)
    else:
        print("Nu exista numere complexe cu modul 10 in lista dumneavoastra")

def menuCautare(l):
    printMenuCautare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        tiparesteParteaImaginara(l)
    elif(n=='2'):
        tiparesteNumereleCuModulSub10(l)
    elif(n=='3'):
        tiparesteNumereleCuModul10(l)


def printMenuOperatii():
    print("Alegeti ce fel de operatie doriti sa faceti:")
    print("     1 pentru a tipari suma numerelor din lista pe intervalul specificat de dumneavoastra")
    print("     2 pentru a tipari produsul numerelor din lista pe intervalul specificat de dumneavoastra")
    print("     3 pentru a tipari lista sortata descrescator dupa partea imaginara")
    print("     x pentru a va intoarce in meniul principal")


def tiparesteSumaNumerelor(l):
    startInterval = input("start interval = ")
    endInterval = input("sfarsit interval = ")
    startInterval = valideaza_pozitie(startInterval, "start interval")
    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
    lengthOfList = getLengthOfList(l)

    startInterval, endInterval = valideaza_interval(lengthOfList, startInterval, endInterval)

    print("Suma dumneavoastra este urmatoarea:")
    print(convertCalculationToDisplay(getSumOfNumbersInInterval(l, startInterval, endInterval)))


def tiparesteProdusulNumerelor(l):
    startInterval = input("start interval = ")
    endInterval = input("sfarsit interval = ")
    startInterval = valideaza_pozitie(startInterval, "start interval")
    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
    lengthOfList = getLengthOfList(l)

    startInterval, endInterval = valideaza_interval(lengthOfList, startInterval, endInterval)

    print("Produsul dumneavoastra este urmatorul:")
    print(convertCalculationToDisplay(getProductOfNumbersInInterval(l, startInterval, endInterval)))


def sorteazaDescrescatorDupaParteaImaginara(l):
    print("Lista sortata descrescator dupa partea imaginara este urmatoarea")
    newList = convertCalculationsListToDisplayList(reverseSortByImaginary(l))
    print(newList)


def menuOperatii(l):
    printMenuOperatii()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        tiparesteSumaNumerelor(l)
    elif(n=='2'):
        tiparesteProdusulNumerelor(l)
    elif(n=='3'):
        sorteazaDescrescatorDupaParteaImaginara(l)


def printMenuFiltrare():
    print("Alegeti ce fel de filtrare doriti sa faceti:")
    print("     1 pentru a elimina din lista numerele complexe la care partea reala este numar prim")
    print("     2 pentru a elimina din lista numerele complexe a caror modul este <, = sau > decat un numar dat")
    print("     x pentru a va intoarce in meniul principal")


def eliminaNumerelePrime(l):
    filterOutPrimeNumbers(l)


def printMenuFiltrareModul():
    print("Alegeti ce fel de filtrare in functie de modul doriti sa faceti:")
    print("     1 pentru a elimina din lista numerele complexe a caror modul este < decat un numar dat")
    print("     2 pentru a elimina din lista numerele complexe a caror modul este > decat un numar dat")
    print("     3 pentru a elimina din lista numerele complexe a caror modul este = cu un numar dat")
    print("     x pentru a va intoarce in meniul principal")


def filtrareModulMaiMic(l):
    print("Va rugam specificati numarul cu care doriti efectuata compararea modulului")
    modul = input("modul = ")
    modul = valideaza_numar(modul, "modul")
    filterModulusLessThan(l, modul)


def filtrareModulMaiMare(l):
    print("Va rugam specificati numarul cu care doriti efectuata compararea modulului")
    modul = input("modul = ")
    modul = valideaza_numar(modul, "modul")
    filterModulusGreaterThan(l, modul)


def filtrareModulEgal(l):
    print("Va rugam specificati numarul cu care doriti efectuata compararea modulului")
    modul = input("modul = ")
    modul = valideaza_numar(modul, "modul")
    filterModulusEqual(l, modul)


def menuFiltrareModul(l):
    printMenuFiltrareModul()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        filtrareModulMaiMic(l)
    elif(n=='2'):
        filtrareModulMaiMare(l)
    elif(n=='3'):
        filtrareModulEgal(l)


def menuFiltrare(l):
    printMenuFiltrare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        eliminaNumerelePrime(l)
    elif(n=='2'):
        menuFiltrareModul(l)


def meniu():
    finish = False
    calculationsList = [complex(2, 5), complex(3, 6), complex(10, 0), complex(15, 2), complex(100, 1), complex(1, 0),
                        complex(1), complex(1), complex(1), complex(1), complex(8, 6)]

    calculationsDict = {
        0: complex(2, 5),
        1: complex(3, 6),
        2: complex(10, 0),
        3: complex(15, 2),
        4: complex(100, 1),
        5: complex(1, 0),
        6: complex(1),
        7: complex(1),
        8: complex(1),
        9: complex(1),
        10: complex(8, 6)
    }
    lastKnownList = createNewListWithSameValues(calculationsList)
    intermediatteList = []
    displayList = convertCalculationsListToDisplayList(calculationsList)
    a = 0
    while not finish:
        displayList = convertCalculationsListToDisplayList(calculationsList)
        printCurrentList(displayList)
        intermediatteList = createNewListWithSameValues(calculationsList)
        printMenu()
        m = input().strip()


        if(m == 'x'):
            exit()
        elif(m=='+'):
            menuAdaugare(calculationsList)
            lastKnownList = createNewListWithSameValues(intermediatteList)
        elif(m=='-'):
            menuModificare(calculationsList)
            lastKnownList = createNewListWithSameValues(intermediatteList)
        elif(m=='?'):
            menuCautare(calculationsList)
            lastKnownList = createNewListWithSameValues(intermediatteList)
        elif(m=='*'):
            menuOperatii(calculationsList)
            lastKnownList = createNewListWithSameValues(intermediatteList)
        elif(m=='/'):
            menuFiltrare(calculationsList)
            lastKnownList = createNewListWithSameValues(intermediatteList)
        elif(m=='u'):
            calculationsList = createNewListWithSameValues(lastKnownList)

        else:
            pass




