# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int (input("Введите общее количество журавликов "))
s = int (a / 6)
n = int (4 * s)
print ("Петя сделал", s, "Катя сделала", n, "Сережа сделал", s)