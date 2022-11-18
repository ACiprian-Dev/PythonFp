from infrastructura.lista_repository import addComplexNumberToList, addComplexNumberAtPosition, \
    removeComplexNumberAtPosition, removeComplexNumbersInInterval, replaceAllOccurrencesOfComplexNumber, \
    convertCalculationsDictionaryToDisplayList, getLengthOfList, getImaginaryPartOfNumbers, \
    getListOfNumbersWithModulusLessThan10, getListOfNumbersWithModulus10, getSumOfNumbersInInterval, \
    convertCalculationToDisplay, getProductOfNumbersInInterval, reverseSortByImaginary, filterOutPrimeNumbers, \
    filterModulusLessThan, filterModulusGreaterThan, filterModulusEqual, createNewListWithSameValues, \
    convertCalculationsListToDisplayList
from validare.validare_numere import valideaza_numar, valideaza_pozitie, valideaza_numar_de_inlocuit, valideaza_interval


def printCurrentList(l, dictionaryLength):
    newList = convertCalculationsDictionaryToDisplayList(l)
    print("Lista dumneavoastra de numere complexe este urmatoarea:")
    print(newList)


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


def adaugaNumarComplex(calculationsList, dictionaryLength, a, b):


    addComplexNumberToList(calculationsList, complex(a,b), dictionaryLength)



def adaugaNumarComplexPePozitie(l, dictionaryLength, a, b, poz):


    addComplexNumberAtPosition(l, complex(a, b), poz, dictionaryLength)


def printMenuModificare():
    print("Alegeti ce fel de modificare doriti sa faceti:")
    print("     1 pentru a sterge un numar complex de pe o pozitie data")
    print("     2 pentru a sterge numerele complexe de pe un interval dat")
    print("     3 pentru a inlocui toate aparitiile unui numar complex cu alt numar complex")
    print("     x pentru a va intoarce in meniul principal")


def stergeNumarComplexPePozitie(l, dictionaryLength, poz):
    removeComplexNumberAtPosition(l,poz, dictionaryLength)


def stergeNumereComplexePeInterval(l, dictionaryLength, startInterval, endInterval):



    removeComplexNumbersInInterval(l, startInterval, endInterval, dictionaryLength)


def inlocuiesteToateAparitiileUnuiNumarComplex(l, dictionaryLength, replacement, numberToReplace):



    replaceAllOccurrencesOfComplexNumber(l, replacement, numberToReplace, dictionaryLength)



def menuModificare(l, dictionaryLength):
    printMenuModificare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        stergeNumarComplexPePozitie(l, dictionaryLength)
    elif(n=='2'):
        stergeNumereComplexePeInterval(l, dictionaryLength)
    elif(n=='3'):
        inlocuiesteToateAparitiileUnuiNumarComplex(l, dictionaryLength)


def printMenuCautare():
    print("Alegeti ce fel de cautare doriti sa faceti:")
    print("     1 pentru a tipari partea imaginara a numerelor din lista de pe intervalul specificat de dumneavoastra")
    print("     2 pentru a tipari toate numerele complexe care au modulul mai mic decat 10")
    print("     3 pentru a tipari toate numerele complexe care au modulul egal cu 10")
    print("     x pentru a va intoarce in meniul principal")


def tiparesteParteaImaginara(l, startInterval, endInterval):

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

def menuCautare(l, dictionaryLength):
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


def tiparesteSumaNumerelor(l, startInterval, endInterval):
    print("Suma dumneavoastra este urmatoarea:")
    print(convertCalculationToDisplay(getSumOfNumbersInInterval(l, startInterval, endInterval)))


def tiparesteProdusulNumerelor(l, startInterval, endInterval):

    print("Produsul dumneavoastra este urmatorul:")
    print(convertCalculationToDisplay(getProductOfNumbersInInterval(l, startInterval, endInterval)))


def sorteazaDescrescatorDupaParteaImaginara(l):
    print("Lista sortata descrescator dupa partea imaginara este urmatoarea")
    newList = convertCalculationsListToDisplayList(reverseSortByImaginary(l))
    print(newList)


def menuOperatii(l, dictionaryLength):
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


def eliminaNumerelePrime(l, dictionaryLength):
    filterOutPrimeNumbers(l, dictionaryLength)


def printMenuFiltrareModul():
    print("Alegeti ce fel de filtrare in functie de modul doriti sa faceti:")
    print("     1 pentru a elimina din lista numerele complexe a caror modul este < decat un numar dat")
    print("     2 pentru a elimina din lista numerele complexe a caror modul este > decat un numar dat")
    print("     3 pentru a elimina din lista numerele complexe a caror modul este = cu un numar dat")
    print("     x pentru a va intoarce in meniul principal")


def filtrareModulMaiMic(l, dictionaryLength, modul):
    filterModulusLessThan(l, modul, dictionaryLength)


def filtrareModulMaiMare(l, dictionaryLength, modul):
    filterModulusGreaterThan(l, modul, dictionaryLength)


def filtrareModulEgal(l, dictionaryLength, modul):
    filterModulusEqual(l, modul, dictionaryLength)


def menuFiltrareModul(l, dictionaryLength):
    printMenuFiltrareModul()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        filtrareModulMaiMic(l, dictionaryLength)
    elif(n=='2'):
        filtrareModulMaiMare(l, dictionaryLength)
    elif(n=='3'):
        filtrareModulEgal(l, dictionaryLength)


def menuFiltrare(l, dictionaryLength):
    printMenuFiltrare()
    n = input().strip()
    if(n=='x'):
        print("Iesim")
    elif(n=='1'):
        eliminaNumerelePrime(l, dictionaryLength)
    elif(n=='2'):
        menuFiltrareModul(l, dictionaryLength)


def meniu():
    finish = False

    calculationsDictionary = {
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
    dictionaryLength = { "length": 11}


    lastKnownDictionary = {}
    lastKnownDictionary.update(calculationsDictionary)
    intermediatteDictionary = {}

    a = 0
    while not finish:

        printCurrentList(calculationsDictionary, dictionaryLength)

        intermediatteDictionary.update(calculationsDictionary)
        #printMenu()
        print("Introduceti comanda dorita")
        m = input().strip()
        words = m.split()
        words[0].lower()

        match words[0]:
            case "exit":
                exit()
            case "add":
                numbers = words[1].split('+')
                if(len(numbers) <= 1):
                    print("\033[91mComanda invalida, va rugam introduceti un numar \033[0m")
                else:
                    a = numbers[0]
                    b = numbers[1][:-1]

                    a = valideaza_numar(a, "a")
                    b = valideaza_numar(b, "b")
                    if a is not None and b is not None:
                        adaugaNumarComplex(calculationsDictionary, dictionaryLength, a, b)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)
            case "add_at":
                temp = words[1].split(',')
                poz = temp[0]
                poz = valideaza_pozitie(poz, "pozitie")
                numbers = temp[1].split('+')
                if (len(numbers) <= 1):
                    print("\033[91mComanda invalida, va rugam introduceti un numar \033[0m")
                else:
                    a = numbers[0]
                    b = numbers[1][:-1]

                    a = valideaza_numar(a, "a")
                    b = valideaza_numar(b, "b")
                    if a is not None and b is not None and poz is not None:
                        adaugaNumarComplexPePozitie(calculationsDictionary, dictionaryLength, a, b, poz)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)
            case "del_at":
                pozitie = words[1]
                pozitie = valideaza_numar(pozitie, "number")
                if pozitie is not None:
                    stergeNumarComplexPePozitie(calculationsDictionary, dictionaryLength, pozitie)
            case "del":
                temp = words[1].split('-')
                if len(temp) <= 1:
                    print("Va rog introduceti un interval")
                else:
                    startInterval = temp[0]
                    endInterval = temp[1]
                    startInterval = valideaza_pozitie(startInterval, "start interval")
                    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
                    startInterval, endInterval = valideaza_interval(dictionaryLength, startInterval, endInterval)
                    if startInterval is not None and endInterval is not None:
                        stergeNumereComplexePeInterval(calculationsDictionary, dictionaryLength, startInterval, endInterval)
                        lastKnownDictionary = {}
                        lastKnownDictionary.update(intermediatteDictionary)
            case "replace":
                numberToReplace = words[1]
                replacement = words[2]
                numbers = words[1].split('+')

                a = numbers[0]
                b = numbers[1][:-1]
                print(b)
                a = valideaza_numar(a, "a")
                b = valideaza_numar(b, "b")

                numberToReplace = complex(a, b)
                numberToReplace = valideaza_numar_de_inlocuit(calculationsDictionary, numberToReplace)
                print("wtf", numberToReplace)
                numbers = words[2].split('+')

                a = numbers[0]
                b = numbers[1][:-1]

                a = valideaza_numar(a, "a")
                b = valideaza_numar(b, "b")
                replacement = complex(a, b)
                if replacement is not None and numberToReplace is not None:
                    inlocuiesteToateAparitiileUnuiNumarComplex(calculationsDictionary, dictionaryLength, replacement, numberToReplace)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)

            case "imaginary":
                temp = words[1].split('-')
                if len(temp) <= 1:
                    print("Va rog introduceti un interval")
                else:
                    startInterval = temp[0]
                    endInterval = temp[1]
                    startInterval = valideaza_pozitie(startInterval, "start interval")
                    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
                    startInterval, endInterval = valideaza_interval(dictionaryLength["length"], startInterval, endInterval)
                    if startInterval is not None and endInterval is not None:
                        tiparesteParteaImaginara(calculationsDictionary, startInterval, endInterval)
                        lastKnownDictionary = {}
                        lastKnownDictionary.update(intermediatteDictionary)
            case "modulos<10":
                tiparesteNumereleCuModulSub10(calculationsDictionary)
            case "modulos=10":
                tiparesteNumereleCuModul10(calculationsDictionary)
            case "sum":
                temp = words[1].split('-')
                if len(temp) <= 1:
                    print("Va rog introduceti un interval")
                else:
                    startInterval = temp[0]
                    endInterval = temp[1]
                    startInterval = valideaza_pozitie(startInterval, "start interval")
                    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
                    startInterval, endInterval = valideaza_interval(dictionaryLength["length"], startInterval, endInterval)
                    if startInterval is not None and endInterval is not None:
                        tiparesteSumaNumerelor(calculationsDictionary, startInterval, endInterval)
                        lastKnownDictionary = {}
                        lastKnownDictionary.update(intermediatteDictionary)
            case "product":
                temp = words[1].split('-')
                if len(temp) <= 1:
                    print("Va rog introduceti un interval")
                else:
                    startInterval = temp[0]
                    endInterval = temp[1]
                    startInterval = valideaza_pozitie(startInterval, "start interval")
                    endInterval = valideaza_pozitie(endInterval, "sfarsit interval")
                    startInterval, endInterval = valideaza_interval(dictionaryLength["length"], startInterval, endInterval)
                    if startInterval is not None and endInterval is not None:
                        tiparesteProdusulNumerelor(calculationsDictionary, startInterval, endInterval)
                        lastKnownDictionary = {}
                        lastKnownDictionary.update(intermediatteDictionary)
            case "sort":
                sorteazaDescrescatorDupaParteaImaginara(calculationsDictionary)
                lastKnownDictionary = {}
                lastKnownDictionary.update(intermediatteDictionary)
            case "filtru_prim":
                eliminaNumerelePrime(calculationsDictionary, dictionaryLength)
                lastKnownDictionary = {}
                lastKnownDictionary.update(intermediatteDictionary)
            case "modul<":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulMaiMic(calculationsDictionary, dictionaryLength, modul)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)
            case "modul>":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulMaiMare(calculationsDictionary, dictionaryLength, modul)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)
            case "modul=":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulEgal(calculationsDictionary, dictionaryLength, modul)
                    lastKnownDictionary = {}
                    lastKnownDictionary.update(intermediatteDictionary)
            case "undo":
                calculationsDictionary = {}
                calculationsDictionary.update(lastKnownDictionary)

        # if(m == 'x'):
        #     exit()
        # elif(m=='+'):
        #     menuAdaugare(calculationsDictionary, dictionaryLength)
        #     lastKnownDictionary = {}
        #     lastKnownDictionary.update(intermediatteDictionary)
        #     print("fuck off", lastKnownDictionary)
        # elif(m=='-'):
        #     menuModificare(calculationsDictionary, dictionaryLength)
        #     lastKnownDictionary = {}
        #     lastKnownDictionary.update(intermediatteDictionary)
        # elif(m=='?'):
        #     menuCautare(calculationsDictionary, dictionaryLength)
        #     lastKnownDictionary = {}
        #     lastKnownDictionary.update(intermediatteDictionary)
        # elif(m=='*'):
        #     menuOperatii(calculationsDictionary, dictionaryLength)
        #     lastKnownDictionary = {}
        #     lastKnownDictionary.update(intermediatteDictionary)
        # elif(m=='/'):
        #     menuFiltrare(calculationsDictionary, dictionaryLength)
        #     lastKnownDictionary = {}
        #     lastKnownDictionary.update(intermediatteDictionary)
        # elif(m=='u'):
        #     calculationsDictionary = {}
        #     calculationsDictionary.update(lastKnownDictionary)
        #
        # else:
        #     pass




