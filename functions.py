
# Функция count_all принимает два списка list_1, list_2
# Функция должна возвращать количество повторяющихся чисел в двух списках

def count_all(list_1, list_2):
    #Вставьте свой код ниже
    set1 = set(list_1)
    set2 = set(list_2)
    return len(set1 & set2)

# Функция count_all принимает список list_1
# Функция должна возвращать количество неповторяющихся чисел в списке

def count_all_one(list_1):
    #Вставьте свой код ниже
    var_set = set(list_1)
    return len(var_set)

# Функция find_val принимает словарь d_1 и ключ k_1
# Функция должна возвращать значение ключа

def find_val(d_1, k_1):
    #Вставьте свой код ниже

    return d_1.get(k_1)

# Функция change_elems принимает список list_1
# Необходимо поменять местами максимальный и минимальный элементы
# Функция должна возвращать измененный список

def change_elems(list_1):
    new_list = []
    #Вставьте свой код ниже
    lst_num = list(enumerate(list_1, 0))
    max_value = max(lst_num, key=lambda i : i[1])
    min_value = min(lst_num, key=lambda i : i[1])
    new_list = list(list_1)
    new_list[max_value[0]] = min_value[1]
    new_list[min_value[0]] = max_value[1]
    return new_list

# Функция find_more принимает список list_1
# Необходимо вытащить все элементы списка, которые больше предыдущего
# Функция должна возвращать список с этими элементами

def find_more(list_1):
    even_list = []
    #Вставьте свой код ниже
    for i in range(len(list_1) - 1):
        if list_1[i+1] > list_1[i]:
            even_list.append(list_1[i+1])
    
    return even_list

# Функция find_even принимает список list_1
# Необходимо вытащить все элементы списка с четными индексами
# Функция должна возвращать список с этими элементами
# Нулевой элемент считается четным

def find_even(list_1):
    even_list = []
    #Вставьте свой код ниже
    for i in range(len(list_1)):
        if i%2 == 0:
            even_list.append(list_1[i])
    return even_list

def pyramide(final):
    n = final
    while i:
        i -= 1
        print('  ' * i, *range(n, i, -1), *range(i + 2, n + 1))