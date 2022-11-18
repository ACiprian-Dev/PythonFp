from infrastructura.lista_repository import addComplexNumberToList, addComplexNumberAtPosition, getLengthOfList, \
    removeComplexNumberAtPosition, removeComplexNumbersInInterval, replaceAllOccurrencesOfComplexNumber, \
    getImaginaryPartOfNumbers, getModulusOfComplexNumber, getListOfNumbersWithModulusLessThan10, \
    getListOfNumbersWithModulus10, getSumOfNumbersInInterval, getProductOfNumbersInInterval, getImaginary, \
    createNewListWithSameValues, reverseSortByImaginary, isNumberPrime, filterOutPrimeNumbers, filterModulusLessThan, \
    filterModulusGreaterThan, filterModulusEqual, myUndo


def ruleaza_teste_numere():
    calculationsDictionary = {}
    lastKnownDictionary = {}
    lastKnownDictionary.update(calculationsDictionary)
    intermediatteDictionary = {}
    intermediatteDictionary.update(calculationsDictionary)
    dictionaryLength = {
        "length" : -1
    }
    displayList = []
    complexNumber = complex(2,3)
    assert (len(calculationsDictionary) == 0)
    addComplexNumberToList(calculationsDictionary, complexNumber, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert(len(calculationsDictionary) == 1)
    assert(calculationsDictionary[0] == complex(2,3))
    addComplexNumberToList(calculationsDictionary, complexNumber, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    addComplexNumberToList(calculationsDictionary, complexNumber, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    a = 4
    b = 5
    poz = 2
    addComplexNumberAtPosition(calculationsDictionary, complex(a,b), poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert(calculationsDictionary[poz] == complex(a,b))
    a = 0
    b = 0
    poz = 3
    addComplexNumberAtPosition(calculationsDictionary, complex(a,b), poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert(calculationsDictionary[poz] == complex(a,b))
    a = 0
    b = 3
    poz = 4
    addComplexNumberAtPosition(calculationsDictionary, complex(a,b), poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (calculationsDictionary[poz] == complex(a,b))
    a = 10
    b = 0
    poz = 5
    addComplexNumberAtPosition(calculationsDictionary, complex(a,b), poz, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (calculationsDictionary[poz] == complex(a,b))

    calculationsDictionary = {}
    dictionaryLength["length"] = -1
    assert (getLengthOfList(calculationsDictionary) == 0)
    addComplexNumberToList(calculationsDictionary, complex(2, 3), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (getLengthOfList(calculationsDictionary) ==1)

    addComplexNumberToList(calculationsDictionary, complex(5, 4), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    removeComplexNumberAtPosition(calculationsDictionary, 0, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (getLengthOfList(calculationsDictionary) == 1)
    assert  (calculationsDictionary[0] == complex(5, 4))

    addComplexNumberToList(calculationsDictionary, complex(3,5), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    addComplexNumberToList(calculationsDictionary, complex(6, 8), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    addComplexNumberToList(calculationsDictionary, complex(9, 10), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    removeComplexNumbersInInterval(calculationsDictionary, 0, 2, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (getLengthOfList(calculationsDictionary) == 1)
    assert (calculationsDictionary[0] == complex(9, 10))
    addComplexNumberToList(calculationsDictionary, complex(9, 10), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    addComplexNumberToList(calculationsDictionary, complex(9, 10), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    addComplexNumberToList(calculationsDictionary, complex(7, 8), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    replaceAllOccurrencesOfComplexNumber(calculationsDictionary, complex(1,1), complex(9,10), dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (calculationsDictionary == {
        0: complex(1,1),
        1: complex(1,1),
        2: complex(1,1),
        3: complex(7,8)
    })

    assert (getImaginaryPartOfNumbers(calculationsDictionary, 0, 2) == [1,1,1])

    assert (getModulusOfComplexNumber(complex(8,6)) == 10.0)

    assert (getListOfNumbersWithModulusLessThan10(calculationsDictionary) == [complex(1,1), complex(1,1), complex(1,1)])

    addComplexNumberToList(calculationsDictionary, complex(8,6), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    assert (getListOfNumbersWithModulus10(calculationsDictionary) == [complex(8,6)])

    assert (getSumOfNumbersInInterval(calculationsDictionary, 0, 2) == complex(3,3))

    assert (getProductOfNumbersInInterval(calculationsDictionary, 0, 2) == complex(-2,2))

    assert (getImaginary(complex(2,3)) == 3.0)

    assert (createNewListWithSameValues(calculationsDictionary) == [complex(1,1), complex(1,1), complex(1,1), complex(7,8), complex(8,6)])

    assert (reverseSortByImaginary(calculationsDictionary) == [complex(7,8), complex(8,6) ,complex(1,1), complex(1,1), complex(1,1)])

    assert (isNumberPrime(3) == True)

    filterOutPrimeNumbers(calculationsDictionary, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    assert (calculationsDictionary == {
        0: complex(1,1),
        1: complex(1,1),
        2: complex(1,1),
        3: complex(8,6)
    })

    filterModulusLessThan(calculationsDictionary, 100.0, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    assert (calculationsDictionary == {})

    addComplexNumberToList(calculationsDictionary, complex(10,50), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    filterModulusGreaterThan(calculationsDictionary, 4.5, dictionaryLength, lastKnownDictionary, intermediatteDictionary)
    assert (calculationsDictionary =={})

    addComplexNumberToList(calculationsDictionary, complex(3,4), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    filterModulusEqual(calculationsDictionary, 5.0, dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    assert (calculationsDictionary == {})

    addComplexNumberToList(calculationsDictionary, complex(5, 4), dictionaryLength, lastKnownDictionary, intermediatteDictionary)

    assert  (calculationsDictionary == {
        0: complex(5, 4)
    })

    myUndo(dictionaryLength, lastKnownDictionary, calculationsDictionary)

    assert (calculationsDictionary == {})

def ruleaza_toate_testele():
    ruleaza_teste_numere()
