# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, 
# Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример
# ноутбук
# 12

p = input('Введите слово - ')
start = set(p)
print (start)
# rus = (А, В, Е, И, Н, О, Р, С, Т, Д, К, Л, М, П, У, Б, Г, Ё, Ь, Я, Й, Ы, Ж, З, Х, Ц, Ч, Ш, Э, Ю, Ф, Щ, Ъ)
# eng = (A, E, I, O, U, L, N, S, T, R, D, G, B, C, M, P, F, H, V, W, Y, K, J, X, Q, Z)
rus_1 = {"А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"}
rus_2 = {"Д", "К", "Л", "М", "П", "У"} 
rus_3 = {"Б", "Г", "Ё", "Ь", "Я"}
rus_4 = {"Й", "Ы"} 
rus_5 = {"Ж", "З", "Х", "Ц", "Ч"}
rus_6 = {"Ш", "Э", "Ю"}
rus_7 = {"Ф", "Щ", "Ъ"}
rus = (rus_1|rus_2|rus_3|rus_4|rus_5|rus_6|rus_7)
eng_1 = {"A", "E", "I", "O", "U", "L", "N", "S", "T", "R"}
eng_2 = {"D", "G"} 
eng_3 = {"B", "C", "M", "P"}
eng_4 = {"F", "H", "V", "W", "Y"} 
eng_5 = {"K"}
eng_6 = {"J", "X"}
eng_7 = {"Q", "Z"}
eng = (eng_1|eng_2|eng_3|eng_4|eng_5|eng_6|eng_7)
dict = {
    1:set(rus_1|eng_1),
    2:set(rus_2|eng_2),
    3:set(rus_3|eng_3),
    4:set(rus_4|eng_4),
    5:set(rus_5|eng_5),
    8:set(rus_6|eng_6),
    10:set(rus_7|eng_7),
}
sum = 0
# print(dict.items())
if set(start).issubset(rus) or set(start).issubset(eng):
    for i in list(p):
        for (k, v) in dict.items():
            if i in v:
                sum+=k
    print (sum)
else:
    print ("неверное слово!")



#     1:["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
#     2:["D", "G"], 
#     3:["B", "C", "M", "P"],
#     4:["F", "H", "V", "W", "Y"], 
#     5:["K"], 
#     8:["J", "X"], 
#     10:["Q", "Z"]
# }

# rus_1 ={
#     1:{"А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"},
#     2:{"Д", "К", "Л", "М", "П", "У"}, 
#     3:{"Б", "Г", "Ё", "Ь", "Я"},
#     4:{"Й", "Ы"}, 
#     5:{"Ж", "З", "Х", "Ц", "Ч"}, 
#     8:{"Ш", "Э", "Ю"}, 
#     10:{"Ф", "Щ", "Ъ"}
# }
# eng_1 ={
#     1:["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
#     2:["D", "G"], 
#     3:["B", "C", "M", "P"],
#     4:["F", "H", "V", "W", "Y"], 
#     5:["K"], 
#     8:["J", "X"], 
#     10:["Q", "Z"]
# }
# print(rus_1.values())