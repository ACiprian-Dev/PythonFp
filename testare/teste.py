from infrastructura.lista_repository import addComplexNumberToList, addComplexNumberAtPosition, getLengthOfList, \
    removeComplexNumberAtPosition, removeComplexNumbersInInterval, replaceAllOccurrencesOfComplexNumber, \
    getImaginaryPartOfNumbers, getModulusOfComplexNumber, getListOfNumbersWithModulusLessThan10, \
    getListOfNumbersWithModulus10, getSumOfNumbersInInterval, getProductOfNumbersInInterval, getImaginary, \
    createNewListWithSameValues, reverseSortByImaginary, isNumberPrime, filterOutPrimeNumbers, filterModulusLessThan, \
    filterModulusGreaterThan, filterModulusEqual


def ruleaza_teste_numere():
    calculationsList= []
    displayList = []
    complexNumber = complex(2,3)
    assert (len(displayList) == 0)
    addComplexNumberToList(calculationsList, complexNumber)
    assert(len(calculationsList) == 1)
    assert(calculationsList[0] == complex(2,3))
    addComplexNumberToList(calculationsList, complexNumber)
    addComplexNumberToList(calculationsList, complexNumber)

    a = 4
    b = 5
    poz = 2
    addComplexNumberAtPosition(calculationsList, complex(a,b), poz)
    assert(calculationsList[poz] == complex(a,b))
    a = 0
    b = 0
    poz = 3
    addComplexNumberAtPosition(calculationsList, complex(a,b), poz)
    assert(calculationsList[poz] == complex(a,b))
    a = 0
    b = 3
    poz = 4
    addComplexNumberAtPosition(calculationsList, complex(a,b), poz)
    assert (calculationsList[poz] == complex(a,b))
    a = 10
    b = 0
    poz = 5
    addComplexNumberAtPosition(calculationsList, complex(a,b), poz)
    assert (calculationsList[poz] == complex(a,b))

    l = []
    assert (getLengthOfList(l) == 0)
    addComplexNumberToList(l, complex(2, 3))
    assert (getLengthOfList(l) ==1)

    addComplexNumberToList(l, complex(5, 4))
    removeComplexNumberAtPosition(l, 0)
    assert (getLengthOfList(l) == 1)
    assert  (l[0] == complex(5, 4))

    addComplexNumberToList(l, complex(3,5))
    addComplexNumberToList(l, complex(6, 8))
    addComplexNumberToList(l, complex(9, 10))

    removeComplexNumbersInInterval(l, 0, 2)
    assert (getLengthOfList(l) == 1)
    assert (l[0] == complex(9, 10))
    addComplexNumberToList(l, complex(9, 10))
    addComplexNumberToList(l, complex(9, 10))
    addComplexNumberToList(l, complex(7, 8))

    replaceAllOccurrencesOfComplexNumber(l, complex(1,1), complex(9,10))
    assert (l == [complex(1,1), complex(1,1), complex(1,1), complex(7,8)])

    assert (getImaginaryPartOfNumbers(l, 0, 2) == [1,1,1])

    assert (getModulusOfComplexNumber(complex(8,6)) == 10.0)

    assert (getListOfNumbersWithModulusLessThan10(l) == [complex(1,1), complex(1,1), complex(1,1)])

    addComplexNumberToList(l, complex(8,6))

    assert (getListOfNumbersWithModulus10(l) == [complex(8,6)])

    assert (getSumOfNumbersInInterval(l, 0, 2) == complex(3,3))

    assert (getProductOfNumbersInInterval(l, 0, 2) == complex(-2,2))

    assert (getImaginary(complex(2,3)) == 3.0)

    assert (createNewListWithSameValues(l) == [complex(1,1), complex(1,1), complex(1,1), complex(7,8), complex(8,6)])

    assert (reverseSortByImaginary(l) == [complex(7,8), complex(8,6) ,complex(1,1), complex(1,1), complex(1,1)])

    assert (isNumberPrime(3) == True)

    filterOutPrimeNumbers(l)
    assert (l == [complex(1,1), complex(1,1), complex(1,1), complex(8,6)])

    filterModulusLessThan(l, 100.0)

    assert (l == [])

    addComplexNumberToList(l, complex(3,4))

    filterModulusGreaterThan(l, 4.5)

    assert (l ==[])

    addComplexNumberToList(l, complex(3,4))
    filterModulusEqual(l, 5.0)

    assert (l == [])

    # assert (myUndo([1,2,3,4,5,7]) == [1,2,3,4,5,7])

def ruleaza_toate_testele():
    ruleaza_teste_numere()

