# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

n = int(input('Введи минимальное значение - '))
m = int(input('Введи максимальное значение - '))
result_list = []
main_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
result_list = [i for i in range (len(main_list)) if main_list[i] >= n and main_list[i] <= m]
# for i in range (len(main_list)):
#     if main_list[i] >= n and main_list[i] >= m:
#         result_list.append[i]
print (result_list)

