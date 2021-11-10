def is_prim(n):
    '''
    Verifica n nr prim
    :param n: nr intreg
    :return: True daca n este prim si False, altfel
    '''
    if n<2:
        return False
    if n==2:
        return True
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True

def test_is_prim():
    assert is_prim(17) == True
    assert is_prim(2) == True
    assert is_prim(-5) == False
    assert is_prim(84) == False

test_is_prim()

def nr_prime(lista):
    '''
    Verifica daca elem listei sunt form din nr prim
    :param lista: list de nr intregi
    :return: True daca elem form sunt prim si False, altfel
    '''
    for x in lista:
        if is_prim(x)==False:
            return False
    return True

def test_nr_prime():
    assert nr_prime([2, 3, 5, 9]) == False
    assert nr_prime([2, 3, 5, 7]) == True

test_nr_prime()

def get_longest_all_primes(l) -> list[int]:
    '''
    Determinarea secventa cea mai lunga cu prop ca nr sunt prime
    :param l: lista de nr intregi
    :return: rez lista care reprezinta secventa de lungime maxima cu prop ca nr sunt prime
    '''
    result = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if nr_prime(l[i:j + 1]) == True and len(l[i:j + 1]) > len(result):
                result = l[i:j + 1]
    return result

def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 2, 3, 4]) == [2, 3]
    assert get_longest_all_primes([10, 11, 13, 12, 13, 14, 15]) == [11, 13]

test_get_longest_all_primes()

def is_even (n):
    '''
    Determina daca numarul dat este par
    :param n: numarul dat
    :return: daca este par returneaza True daca nu este par returneaza False
    '''
    if n % 2 == 0:
        return True
    return False

def test_is_even():
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(8) == True
    assert is_even(7) == False

test_is_even()

def get_even(lista):
    '''
    Determina daca toate numerele sunt pare
    :param lista: lista de numere
    :return: lista cu numere pare
    '''
    result = []
    for x in lista:
        if is_even(x):
            result.append(x)
    return result
    

def get_longest_all_even(l):
    '''
    Determina cea mai lunga subsecventa a unei liste cu proprietatea ca toate numerele sunt pare
    :param l: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    result = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            all_even = True
            for x in l[i:j + 1]:
                if x % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if i - j + 1 > len(result):
                     result = l[i:j + 1]
    return result

def test_get_longest_all_even():
    assert get_longest_all_even([12, 13, 155, 211]) == [12]
    assert get_longest_all_even([5, 6, 7]) == [6]

test_get_longest_all_even()

def is_nr_div(n):
    '''
    Determina numarul de divizori al numarului dat
    :param n: Numarul dat
    :return: Variabila k care returneaza numarul total de divizori al numarului.
    '''
    k = 0
    x = n
    for i in range(1, x + 1):
        if x % i == 0:
            k = k+1
    return k

def test_is_nr_div():
    assert is_nr_div(11) == 2
    assert is_nr_div(8) == 4
    assert is_nr_div(5) == 2

test_is_nr_div()

def get_nr_div(lista):
    '''
    Determina daca toate numerele au acelasi numar de divizori
    :param lista: lista cu numere
    :return: lista cu numerele care au acelasi numar de divizori
    '''
    result = []
    for x in lista:
        if is_nr_div(x):
            result.append(x)
    return result

def get_longest_same_div_count(l):
    '''
    Determina cea mai lunga subsecventa in care numerele au acelasi numar de divizori
    :param l: Lista in care se cauta subsecventa
    :return: Subsecventa gasita
    '''
    result = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            k = is_nr_div(l[i])
            all_same_div_count = True
            for x in l[i:j + 1]:
                if is_nr_div(x)!=k:
                    all_same_div_count = False
                    break
            if all_same_div_count:
                if i - j + 1 > len(result):
                     result = l[i:j + 1]
    return result

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([7, 25, 44]) == [7]
    assert get_longest_same_div_count([12, 81,2]) == [12]

test_get_longest_same_div_count()

def show_menu():
    print('''
    1. Citire 
    2. Cea mai lunga secventa cu proprietatea ca toate numerele sunt formate din cifre prime
    3. Cea mai lunga secventa cu proprietatea ca toate numerele din lista sunt pare
    4. Cea mai lunga secventa cu proprietatea ca toate numerele din lista au acelasi numar de divizori
    5. Iesire
    ''')

def read_list():
    lst = []
    n = int(input("Numarul de elemente"))
    for i in range(n):
        x = int(input("a[{}]=".format(i + 1)))
        lst.append(x)
    return lst

def run_UI():

    lista = []
    while True:
        show_menu()
        cmd = input("Comanda:")
        if cmd == '1':
            lista = read_list()
        else:
            if cmd == '2':
                list_nr_prime = get_longest_all_primes(lista)
                print(list_nr_prime)
            elif cmd == '3':
                list_longest_all_evens = get_longest_all_even(lista)
                print(list_longest_all_evens)
            elif cmd == '4':
                list_div_count = get_longest_same_div_count(lista)
                print(list_div_count)
            elif cmd == '5':
                break
            else:
                print("Comanda invalida")

run_UI()