def valideaza_tip_numar(numar):
    '''
    Valideaza faptul ca parametrul numar este un numar
    :param numar: any type
    :return: returneaza numarul numar sau un mesaj de atentionare
    '''
    errors = ""
    try:
        val = int(numar)
    except ValueError:
        try:
            val = float(numar)
        except ValueError:
            val = False

    if type(val) != bool:
        return val
    else:
        return "\033[91mInputul dumneavoastra nu este numar, va rugam introduceti un numar\033[0m"

def valideaza_numar(numar, tipDeValidare):
    '''
    Valideaza un numar introdus de user si il atentioneaza in cazul in care type-ul inputului este gresit
    :param numar: un numar(int/float)
    :param tipDeValidare: numele parametrului care este validat
    :return: un numar
    '''
    temp = valideaza_tip_numar(numar)
    if type(temp) == str:
        print(temp)
    else:
        return temp



def valideaza_numar_intreg(numar):
    '''
    Verifica daca numarul numar este numar intreg
    :param numar: un numar
    :return: un numar intreg sau mesaj de avertizare
    '''
    try:
        val = int(numar)
    except:
        val = False
    if(type(val)!=bool):
        return val
    else:
        return "\033[91mInputul dumneavoastra nu este un numar intreg, va rugam introduceti un numar intreg\033[0m"

def valideaza_pozitie(pozitie, tipDeValidare):


    temp = valideaza_tip_numar(pozitie)
    if type(temp) == str:
        print(temp)
    else:
        return temp


def valideaza_interval(lengthOfList, startInterval, endInterval):
    '''
    Verifica ca intervalul introdus de utilizator este valid
    :param lengthOfList: lungimea listei in care se cauta intervalul
    :param startInterval: pozitia de inceput a intervalului
    :param endInterval: pozitia de  final a intervalului
    :return: startInterval, endInterval
    '''


    while True:
        if (startInterval < 0):
            print("Intervalul trebuie nu poate incepe de pe o pozitie negativa")
            startInterval = int(input("start interval = "))
        elif (endInterval > lengthOfList):
            print("Intervalul dat de dumneavoastra depaseste lungimea listei")
            endInterval = int(input("sfarsit interval = "))
        elif (startInterval > endInterval):
            print(
                "Pozitia de start a intervalului dumneavoastra nu poate fi mai mare decat pozitia de sfarsit a intervalului")
            startInterval = int(input("start interval = "))
        else:
            break

    return startInterval, endInterval

def valideaza_numar_de_inlocuit(l, numberToReplace):
    '''
    Verifica ca numarul numberToReplace exista in lista l
    :param l: lista de numere complexe
    :param numberToReplace: numar complex
    :return: numberToReplace
    '''
    while True:
        if(numberToReplace in l.values()):
            break;
        else:
            print("Numarul specificat de dumneavoastra nu exista in lista, va rugam introduceti alt numar")
            print("Specificati ce numar complex doriti sa inlocuiti")
            a = input("Partea reala a numarului de inlocuit = ")
            a = valideaza_numar(a, "a")
            b = input("Partea imaginara a numarului de inlocuit = ")
            b = valideaza_numar(b, "b")
            numberToReplace = complex(a, b)

    return numberToReplace