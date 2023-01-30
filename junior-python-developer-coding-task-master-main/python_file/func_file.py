#Функция для удаления нужного столбца в списке
def del_column(arr, index):
    for row in arr:
        row.pop(index)
    return arr


#Функция для удаления из списка элементов первой строки которые не являются общими с другими списками
def filter_arr(arr, common_elements_end):
    try:
        # Создаем дубликат списка для корректного выявления элементов которые нужно удалить
        search_j_arr = []
        for j in arr[0]:
            search_j_arr.append(j)

        for j in search_j_arr:
            if j not in common_elements_end:  # Нашли элемент который нужно удалить
                for i in arr[0]:  # Ищем этот элемент в списке
                    if i == j:
                        del_column(arr, iter)  # Вызываем функцию для удаления нужного столбца
                    iter += 1  # Счетчик для последующего запоминания индекса элемента в списке
            iter = 0
    except Exception as e:
        print('ERROR - %s' % e)


# Функция для сортировки списока в алфавитном порядке пузырьковым методом
def sort_arr(arr, len_column_arr):
    len_arr = len(arr[0])
    for i in range(len_arr):
        for j in range(i + 1, len_arr):
            if arr[0][i] > arr[0][j]:
                arr[0][i], arr[0][j] = arr[0][j], arr[0][i]
                for z in range(1, len_column_arr):
                    arr[z][i], arr[z][j] = arr[z][j], arr[z][i]


# Сортируем список по первому элементу каждой
def sort_arr_basic(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        for j in range(len_arr-i):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Складываем значения M1-Mn у D1-Dn с имеющих одинаковые значения, и удаляем одинаковые строки по D1-Dn
def sort_arr_advanced(arr):
    iter = 0
    # Считаем количество символов в строке, которые относятся к D1-Dn
    for i in arr[1]:
        if i.isdigit():
            break
        iter += 1

    len_arr_row = len(arr)
    len_arr_column = len(arr[0])
    flag_sum = True
    elements_not_new_arr = []

    for i in range(1, len_arr_row):
        for j in range(1, len_arr_row-i):
            flag_sum = True
            if i != j:
                for k in range(iter):      # Сравниваем строки между собой
                    if arr[i][k] != arr[j][k]:
                        flag_sum = False

                if flag_sum:  # Если две строки равны между собой тогда складываем значения их D1-Dn
                    if arr[j] not in elements_not_new_arr:
                        for k in range(iter, len_arr_column):
                            arr[i][k] = int(arr[i][k])
                            arr[j][k] = int(arr[j][k])
                            arr[i][k] += arr[j][k]
                        elements_not_new_arr += [arr[j]]
    new_arr = []
    [new_arr.append(item) for item in arr if item not in new_arr] # Убираем из списка повторяющиеся элементы
    new_arr.sort()

    len_new_arr0 = len(new_arr[0])
    # Меняем названия Mn на MSn
    for i in range(len_new_arr0):
        if new_arr[0][i][0] == 'M':
            new_arr[0][i] = str(new_arr[0][i][:1]) + 'S' + str(new_arr[0][i][1:])

    return new_arr








