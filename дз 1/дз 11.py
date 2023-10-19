def concatenate_languages(L1, L2):
    if not (0 < len(L1) <= 10000): #проверка на длину массива
        print("Ошибка: L1 должен иметь не менее 1 и не более 10 000 элементов")
        return []

    if not (0 < len(L2) <= 10000):
        print("Ошибка: L2 должен иметь не менее 1 и не более 10 000 элементов")
        return []

    for chain1 in L1: #проверка на тип и на длину цепочек
        if not isinstance(chain1, str) or len(chain1) > 100:
            print(f"Ошибка: Входящая цепочка '{chain1}' в L1 не типа string или содержит более 100 символов")
            return []

    for chain2 in L2:
        if not isinstance(chain2, str) or len(chain2) > 100:
            print(f"Ошибка: Входящая цепочка '{chain2}' в L1 не типа string или содержит более 100 символов")
            return []

    result_language = [] #результирующий массив

    for chain1 in L1: #конкатенация языков
        for chain2 in L2:
            result_language.append(chain1 + chain2)

    return result_language

# входные данные:
L1 = ["fghioigf", "defgsdfghjh", "ijklmnosdfg"]
L2 = ["adwuqgnjimkdbpkezsujnlxcxjeipfrkgsehrjhfukji", "5678dfg9", "uvwxygtyt4567yz"]

# конкатенация
result_language = concatenate_languages(L1, L2)

if result_language:
    # вывод
    for chain in result_language:
        print(chain)
