from infrastructura.lista_repository import addComplexNumberToList, addComplexNumberAtPosition, \
    removeComplexNumberAtPosition, removeComplexNumbersInInterval, replaceAllOccurrencesOfComplexNumber, \
    convertCalculationsDictionaryToDisplayList, getLengthOfList, getImaginaryPartOfNumbers, \
    getListOfNumbersWithModulusLessThan10, getListOfNumbersWithModulus10, getSumOfNumbersInInterval, \
    convertCalculationToDisplay, getProductOfNumbersInInterval, reverseSortByImaginary, filterOutPrimeNumbers, \
    filterModulusLessThan, filterModulusGreaterThan, filterModulusEqual, createNewListWithSameValues, \
    convertCalculationsListToDisplayList, myUndo
from validare.validare_numere import valideaza_numar, valideaza_pozitie, valideaza_numar_de_inlocuit, valideaza_interval


def printCurrentList(l, dictionaryLength):
    newList = convertCalculationsDictionaryToDisplayList(l)
    print("Lista dumneavoastra de numere complexe este urmatoarea:")
    print(newList)

def adaugaNumarComplex(calculationsList, dictionaryLength, a, b, lastKnownDictionary, intermediatteDictionary):


    addComplexNumberToList(calculationsList, complex(a,b), dictionaryLength,lastKnownDictionary, intermediatteDictionary)



def adaugaNumarComplexPePozitie(l, dictionaryLength, a, b, poz, lastKnownDictionary, intermediatteDictionary):


    addComplexNumberAtPosition(l, complex(a, b), poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

def stergeNumarComplexPePozitie(l, dictionaryLength, poz, lastKnownDictionary, intermediatteDictionary):
    removeComplexNumberAtPosition(l,poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)


def stergeNumereComplexePeInterval(l, dictionaryLength, startInterval, endInterval, lastKnownDictionary, intermediatteDictionary):



    removeComplexNumbersInInterval(l, startInterval, endInterval, dictionaryLength, lastKnownDictionary, intermediatteDictionary)


def inlocuiesteToateAparitiileUnuiNumarComplex(l, dictionaryLength, replacement, numberToReplace, lastKnownDictionary, intermediatteDictionary):



    replaceAllOccurrencesOfComplexNumber(l, replacement, numberToReplace, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

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

def eliminaNumerelePrime(l, dictionaryLength, lastKnownDictionary, intermediatteDictionary):
    filterOutPrimeNumbers(l, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

def filtrareModulMaiMic(l, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary):
    filterModulusLessThan(l, modul, dictionaryLength, lastKnownDictionary, intermediatteDictionary)


def filtrareModulMaiMare(l, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary):
    filterModulusGreaterThan(l, modul, dictionaryLength, lastKnownDictionary, intermediatteDictionary)


def filtrareModulEgal(l, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary):
    filterModulusEqual(l, modul, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

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
                if len(numbers) <= 1:
                    print("\033[91mComanda invalida, va rugam introduceti un numar \033[0m")
                else:
                    a = numbers[0]
                    b = numbers[1][:-1]

                    a = valideaza_numar(a, "a")
                    b = valideaza_numar(b, "b")
                    if a is not None and b is not None:
                        adaugaNumarComplex(calculationsDictionary, dictionaryLength, a, b, lastKnownDictionary, intermediatteDictionary)
            case "add_at":
                temp = words[1].split(',')
                poz = temp[0]
                poz = valideaza_pozitie(poz, "pozitie")
                numbers = temp[1].split('+')
                if len(numbers) <= 1:
                    print("\033[91mComanda invalida, va rugam introduceti un numar \033[0m")
                else:
                    a = numbers[0]
                    b = numbers[1][:-1]

                    a = valideaza_numar(a, "a")
                    b = valideaza_numar(b, "b")
                    if a is not None and b is not None and poz is not None:
                        adaugaNumarComplexPePozitie(calculationsDictionary, dictionaryLength, a, b, poz, lastKnownDictionary, intermediatteDictionary)
            case "del_at":
                pozitie = words[1]
                pozitie = valideaza_numar(pozitie, "number")
                if pozitie is not None:
                    stergeNumarComplexPePozitie(calculationsDictionary, dictionaryLength, pozitie, lastKnownDictionary, intermediatteDictionary)
            case "del":
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
                        stergeNumereComplexePeInterval(calculationsDictionary, dictionaryLength, startInterval, endInterval, lastKnownDictionary, intermediatteDictionary)
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
                numbers = words[2].split('+')

                a = numbers[0]
                b = numbers[1][:-1]

                a = valideaza_numar(a, "a")
                b = valideaza_numar(b, "b")
                replacement = complex(a, b)
                if replacement is not None and numberToReplace is not None:
                    inlocuiesteToateAparitiileUnuiNumarComplex(calculationsDictionary, dictionaryLength, replacement, numberToReplace, lastKnownDictionary, intermediatteDictionary)

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
            case "sort":
                sorteazaDescrescatorDupaParteaImaginara(calculationsDictionary)
            case "filtru_prim":
                eliminaNumerelePrime(calculationsDictionary, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
            case "modul<":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulMaiMic(calculationsDictionary, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary)
            case "modul>":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulMaiMare(calculationsDictionary, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary)
            case "modul=":
                modul = words[1]
                modul = valideaza_numar(modul, "modul")
                if modul is not None:
                    filtrareModulEgal(calculationsDictionary, dictionaryLength, modul, lastKnownDictionary, intermediatteDictionary)
            case "undo":
                myUndo(dictionaryLength, lastKnownDictionary, calculationsDictionary)
            case _:
                print("Comanda invalida")






