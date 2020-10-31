def binary_search(list, item): # В переменных low и high хранится границы той части списка в которой выпоняется поиск 
    low = 0
    high = len(list)-1

    while low <= high:  # Пока эта часть не сократится до определенного момента ...
        mid = (low + high) # ...проверяем средний элемент 
        guess = list[mid]
        if guess == item: # Значение найдено
            return mid
        if guess > item: # Много
            high = min - 1
        else:            #  Мало
            low = mid + 1
    return None          # Значение не существует 
my_list = [1, 3, 5, 7, 9]  # Тестируем функцию 

print binary_search(my_list, 3) # => 1 Нумирация элементов начинается с 0 Второй ячейке соответсвет индекс 1 
print binary_search(my_list, -1) # => None озночает Ничто это признак того что элемент не найден 

