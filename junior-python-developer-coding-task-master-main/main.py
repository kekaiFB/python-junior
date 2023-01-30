import os
import csv
from python_file.func_file import sort_arr, filter_arr, sort_arr_basic, sort_arr_advanced
from python_file.open_file import file_csv, file_json, file_xml
import glob

all_arr = []

# Открываем все файлы с нужным расширением, и добавляем их в виде списков
filename_csv = glob.glob('*.csv')
for file in filename_csv:
    all_arr += [file_csv(file)]

filename_json = glob.glob('*.json')
for file in filename_json:
    all_arr += [file_json(file)]

filename_xml = glob.glob('*.xml')
for file in filename_xml:
    all_arr += [file_xml(file)]


count_arr =len(all_arr) # Количество списков
common_elements = [] # Для того чтобы найти общие D1-Dn, M1-Mn
len_arr = [] # Для нахождения длины каждого из списков, для дальнейшей сортировки
arr_finall = [] # Для обьединения всех данных в один список

for i in range(count_arr-1):
    # Найдем общие элементы D1-Dn, M1-Mn в каждом списке
    common_elements = list(set(all_arr[i][0]) & set(all_arr[i+1][0]))
common_elements.sort()


for i in range(count_arr):
    # Удаляем из каждого списка элементы первой строки(D1-Dn, M1-Mn) которые не являются общими с другими списками
    filter_arr(all_arr[i], common_elements)

    # Находим длину каждого списка, для последующей сортировки
    len_arr.append(len(all_arr[i]))

    # Сортировка каждого списока в алфавитном порядке
    sort_arr(all_arr[i], len_arr[i])


for i in range(1, count_arr):
    # Убираем лишние ['D1', 'D3', 'D2', 'M1', 'M2', 'M4', 'M3']
    del all_arr[i][0]

for i in range(count_arr):
    # Соединяем все в один список
    arr_finall += all_arr[i]



try:
    csv.writer(open('basic_result0.tsv', 'w+'), delimiter='\t').writerows(sort_arr_basic(arr_finall))
    with open('basic_result0.tsv') as input, open('basic_result_my.tsv', 'w', newline='') as output:
        writer = csv.writer(output)
        for row in csv.reader(input):
            if any(field.strip() for field in row):
                writer.writerow(row)

    os.remove('basic_result0.tsv')
except IOError as e:
    print('ERROR - cant find file: %s' % e)

try:
    csv.writer(open('advanced_results_my0.tsv', 'w+'), delimiter='\t').writerows(sort_arr_advanced(arr_finall))
    with open('advanced_results_my0.tsv') as input, open('advanced_results_my.tsv', 'w', newline='') as output:
        writer = csv.writer(output)
        for row in csv.reader(input):
            if any(field.strip() for field in row):
                writer.writerow(row)

    os.remove('advanced_results_my0.tsv')
except IOError as e:
    print('ERROR - cant find file: %s' % e)