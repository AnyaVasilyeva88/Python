# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве - "))
list = []
for i in range (n):
    p = int (input("Введите число - "))
    list.append (p)
l = int(input("Введите контрольное значение - "))
for i in range (len(list)):
    if list[i] == l or list[i]+1 == l or list[i]-1 == l:
        print (list[i])
        break
    elif min(list) > l:
        print (min(list))
        break
else:
    print (max(list)) 
        





    