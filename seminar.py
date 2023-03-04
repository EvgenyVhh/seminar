#HOMEWORK
import random

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input('input start num '))
# d = int(input('input step '))
# n = int(input('input max quantity '))
# list_1 = []
# for i in range(n):
#     an = (a1 + i * d)
#     list_1.append(an)
# print(list_1)
#





#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

#
# size = int(input('Input size '))
# list_1 = [random.randint(0,10) for _ in range(size)]
# print(list_1)
# list_2 = []
# min = int(input('input min quantity '))
# max = int(input('inpit max quantity '))
# for i in range (len(list_1)):
#     if min <= list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
#















#
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#



# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

#
# def step(a, b):
#     if b == 1:
#         return (a)
#     if b != 1:
#         return (a * step(a, b -1))
# a = int(input('input A '))
# b = int(input('input B '))
# print(step(a,b))
#
#





# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

# def sum_req(a,b):
#     if a == 0:
#         return b
#     else:
#         return sum_req(a - 1, b + 1)
# a = int(input('input A '))
# b = int(input('input B '))
# print(sum_req(a,b))
#
#








# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input('введите максимальный рамзер списка n: '))
# list_1 = list()
# for i in range(n):
#     x = int(input('введите Значения списка n:'))
#     list_1.append(x)
#
# m = int(input('введите максимальный рамзер списка m: '))
# list_2 = list()
# for i in range(m):
#     y = int(input('введите Значения списка m:'))
#     list_2.append(y)
# print(list_2)
# print(list_1)
# from collections import Counter
#
# common_items = list((Counter(list_1) & Counter(list_2)).elements())
# print('перечения: ', common_items)
#



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

#
# n = int(input('количество кустов :'))
# arr = list()
# for i in range(n):
#     x = int(input('количество ягод на кусте'))
#     arr.append(x)
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr [i +1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print('максимлаьное количество ягод', (max(arr_count)))





# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

# n = int(input('введите максимальный рамзер списка: '))
# list_1 = list()
# for i in range(n):
#     m = int(input('введите Значения списка:'))
#     list_1.append(m)
# count = 0
# x = int(input('search num:'))
# for i in range(len(list_1)):
#     if list_1[i] == x:
#         count +=1
# print(count)
#
#




# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5


# n = int(input('введите максимальный рамзер списка: '))
# list_1 = list()
# for i in range(n):
#     m = int(input('введите Значения списка:'))
#     list_1.append(m)
#
# k = int(input('введите искомое число: '))
# a = abs(k - list_1[0])
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if a >abs(list_1[i] - k):
#         n = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)






#
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

#
# scrum_rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4:'ЙЫ' , 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ' }
# scrum_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'Q, Z'}
# word = input('input search word:').upper()
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in scrum_eng:
#             if i in scrum_eng[j]:
#                 count = count + j
#     else:
#         for j in scrum_rus:
#             if i in scrum_rus[j]:
#                  count = count + j
# print('количество очков = ', count)
#










# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('input number of coins: '))
# count_eagle = 0
# count_tails = 0
# i = int(0)
# for i in range(n):
#     x = int(input('input only 0 or 1:'))
#     if x == 0:
#         count_eagle += 1
#     else:
#         count_tails += 1
# if count_tails > count_eagle:
#     print('minimum number of turns', count_eagle)
# else:
#     print('minimum number of turns', count_tails)
#









# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# x = int(input('input sum:'))
# y = int(input('input product of numbers'))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print('Задуманные Петей числа :', i,',',  j)







# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#
# n = int(input('input N '))
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
















# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# i = int(input('Input three-digit number:  '))
# b = (i // 10)
# print((i // 100) + (b % 10) + (i % 10))






# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10




# cranes = int(input('Input number of cranes:  '))
# petya = int(cranes / 3 / 2)
# serega = int(cranes / 3 / 2)
# katya = int((petya + serega)*2)
#
# print('Petya made', petya)
# print('Katya made', katya)
# print('Serega made', serega)





# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

# num_tic = int(input('Input a number ticket please: '))
# b = num_tic//1000
# one = b//100
# two = (b//10)%10
# three = b%10
# c = num_tic%1000
# four = c//100
# five = (c//10)%10
# six = c%10
# if (one+two+three)==(four+five+six):
#     print('Счастливый Билет')
# else:
#     print('Обычный Билет')





# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
# n = int(input('input size n= '))
# m = int(input('input size m= '))
# k = int(input('input quantity slice= '))
#
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('Yes')
# else:
#     print('No')










#                                                  CLASSWORK


# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
# n = 700
# m = 750
# k = (m + n -1) //n
# print (k)


#
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = 20
# b = 21
# c = 22
# print(((a +1) // 2)+((b + 1) // 2)+((c  + 1)// 2))
#
#

# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6
#
# i = int(input('zashel v kakoi vagon:  ?'))
# j = int(input('vagon realno:  '))
# if i==j:
#     print('malo info')
# else:
#     print(i+j-1)








# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# year = int(input('input year: '))
# if(year%4 ==0 and year%100 != 0 or year % 400 == 0):
#     print("Visokosnyi god")
# else:
#     print("ne visokosnyi god")





# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
#
#
# Input:       5
#
# Output:    120



# n = int(input('Input N: '))
# i = 1
# fact = 1
# while i <= n:
#     fact = i * fact
#     i += 1
# print(f'factorial {n} =  {fact}')
#











# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#
# Input:     5
#
# Output:  6


# number_a = int(input('input a:'))
# a = 0
# b = 1
# count = 2
# while b < number_a:
#     c = a + b
#     a = b
#     b = c
#     count +=1
# if number_a == b:
#     print(count)
# else:
#     print(-1)









# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
#
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
#


# n = int(input('input number days '))
# temp = []
# for i in range(n):#диапозон
#    t = int(input('введите температуру От -50 до +50 '))
#    temp.append(t) #Добавит в конец массива
# count = 0
# maxcount = 0
# flag = False
# for i in temp:
#     if not -50< i < 50:
#         print('error')
#         flag = True
#         break
#     if i >= 0:
#         count +=1
#     else:
#         if maxcount < count:
#             maxcount = count
#         count = 0
# if maxcount < count:
#     maxcount = count
# if not flag:
#     print('max days ', maxcount)



#
# n = int(input("Введите число арбузов  : "))
# m = 1
# while m <= n:
#     mass = int(input("Масса арбуза: "))
#     if m == 1:
#         max_mass = mass
#         min_mass = mass
#     else:
#         if max_mass < mass:
#             max_mass = mass
#         if min_mass > mass:
#             min_mass = mass
#     m += 1
# print(f'Самый тяжелый: {max_mass},Самый  легкий: {min_mass}')
#

#
# 2 вариант
#
# n = int(input("Введите число арбузов  : "))
# temp = []
# for i in range(n):
#     t = int(input('Введите массу арбуза: '))
#     temp.append(t)
# print(min(temp), max(temp))



# СПИСКИ



# list_1 = [1 , 5]
# print(list_1)
# list_1.append(8)#добавление в конец списка нового элемента
# print(list_1)
# list_1.append(85)
# print(list_1)



# list_1 = []
# for i in range(15):
#     list_1.append(i)
#     print(list_1)

#
# list_1 = [1 , 5, 12, 18, 15, 33]
# print(list_1)
# print(list_1.pop())#delite
# print(list_1)
# print(list_1.insert(1, 555))#dobavlenie
# print(len(list_1))#dlina spiska
# print(list_1[0:len(list_1):3])#пройти от начала списка до его конца с шагом 3


# КОРТЕЖИ
#
#
# t = ()
# print(type(t))
# t = (12, )
# print(type(t))
# v = [1, 2, 3,]
# print(type(v))
# v = tuple(v)#perepresvaivanie v tuple
# print(v)
# print(type(v))
# a, b, c = v
# print(a, b, c)

#
# СЛОВАРИ
#
# d = {} # == d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d['q'])




# dict = {}
# dict = {'up' : '↑', 'down': '↓'}
# print(dict)
# for item in dict:
#     print('{}:{}'.format(item, dict[item]))# vivod danih krasivo
#
# del dict['up']#delite
# print(dict)



# Множества

# colors = {'red' , 'green' , 'blue'}
# print(colors)
# colors.add('violet')
# print(colors)
# colors.remove('red')#==dicrard
# print(colors)



# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
#




# list_1 = []
# n = int(input('input limit: ' ))
# for i in range(n):
#     list_1.append(int (input()))
#
# list_1 = set(list_1)
# print(list_1)
# print('Различные элементы:', len(list_1))




# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# list_1 = []
# n = int(input('input limit: ' ))
# for i in range(n):
#     list_1.append(int (input()))
# print(list_1)
# for i in range(int(input())% n):
#     a = list_1.pop(-1)
#     list_1.insert(0, a)
# print(list_1)




# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# print(a[0]['V'])#dostat znach
# b = set()
# for i in a:
#     for j in i:
#         b.add(i[j])
# print(b)
#


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)



# a = [0, -1, 5, 2, 3, -2]
# count = 0
# for i in range(len(a)):
#     if a[i] > a[-1 -i]:
#         count += 1
# print(count)



# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# n = str(input('input: ').split())
#
# a = {}
# for i in n:
#     if i in a:
#         print(f'{i}_{a[i]}', end = ' ')
#     else:
#         print(i, end = ' ')
#     a[i] = a.get(i, 0) + 1
#



# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# n = input('input: ').upper().split()
# m = set(n)
# print(len(m))
#

# Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

# n = int(input('input num'))
# m_max = 0
# while n != 0:
#     n = int(input('input num:'))
#     if m_max < n:
#         m_max = n
# print(m_max)






#ФУНКЦИИ
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res +=i
#     return res
# print(sumnumbers(5))





# def sumnumbers(n):#функция
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# print(sum_str('q','e','eq','qeqeqeqe'))
#
#


# import module# импорт модуля
# print(module.max1(18, 9)) #вызов функции из модуля

# from module import max1 #вызов модуля и его функции
# print(max1(1025525, 1025525))

# import module as m1#переизменование модуля
# print(m1.max1(8,12))


#рекурсии____
#
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print((list_1))


#Алгоритмы________


# def quick_sort(array): #сортировка по возврастанию(быстрая)
#     if len(array) <= 1:
#         return array
#     else:
#         pivat = array[0]
#     less = [i for i in array[1:] if i <= pivat]
#     greater = [i for i in array[1:] if i > pivat]
#     return quick_sort(less) + [pivat] + quick_sort(greater)
#
# print(quick_sort([10,5,2]))


# def merge_sort(nums):# сортировка делением(слияние)
#     if len(nums) > 1:
#         nid = len(nums) //2
#         left = nums[:nid]
#         right = nums[nid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i +=1
#             else:
#                 nums[k] = right[j]
#                 j +=1
#             k +=1
#         while i < len(left):
#             nums[k] = left[i]
#             i +=1
#             k +=1
#         while j < len(right):
#             nums[k] = right[j]
#             j +=1
#             k +=1
# list_1 = [1,5,5,8,6,12,8,5,8,5]
# merge_sort(list_1)
# print(list_1)







# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
#
# Задание необходимо решать через рекурсию




# def fib(n):
#     if n in [0,1]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list_1 = [0]
# for i in range(int(input('input n ' ))):
#     list_1.append(fib(i))
# print((list_1))
# print((list_1[i]))
#







# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


# list_1 = [1, 3, 3, 4, 1]
# max_o = max(list_1)
# min_o = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_o:
#         list_1[i] = min_o
# print(list_1)





# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
#
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
#
#
# Input: 5
#
# Output: yes

#
# def simple(a):
#     for i in range(2,  a):
#         if a%i == 0:
#             return False
#     return True
# if simple(int(input('input num '))):
#     print('yes')
# else:
#     print('no')





# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).


# n = int(input('input n '))
# def f(n):
#
#     if n == 0:
#         return ""
#     m = int(input('input num_s'))
#     return f(n - 1) + f' {m}'
#
# print(f(n))




# ____функции высшего порядка




# def f(x):
#     return x*x
# a = f
# print(type(f))

# def calc1(a, b):
#     return a + b
# def calc2(a, b):
#     return a*b
# def math(op, x, y):## op - передача функции
#     print(op(x,y))
# math(calc2,5, 45)

# calc1= lambda a,b: a + b
# math(calc1, 5 , 45)

# data = [1, 2, 3, 5, 8, 15, 25, 38]
# res = list()
# for i in data:
#     if i % 2 ==0:
#         res.append((i, i**2))
# print(res)


# def select(f, col):
#     return [f(x) for x in col]
# def where(f , col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 25, 38]
# res = select(int,data )
# print(res)
# res = where(lambda  x: x %2 ==0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)
#

# ФУНКЦИЯ MAP____________



# list_1 = [x for x in range (1,20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)







# data = '15 156 98 5 65 85 2'
# print(data)
# # data = data.split()
# # print(data)
# data = list(map(int, data.split()))
# print(data)



# функция FILTER

# data = [15, 60, 9, 16, 175]
# res = list(filter(lambda x: x %10 ==5, data))
# print(res)

# функция ZIP

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна


# list_planets = [(2, 3), (4, 7), (3, 3),
#                 (7, 6), (1, 8), (2, 2),
#                 (5, 6), (6, 3), (2, 8)]
#
#
# list_planets_2 = []
#
# for i in range(len(list_planets)):
#     if list_planets[i][0] != list_planets[i][1]:
#         list_planets_2.append(list_planets[i][0]*list_planets[i][1])
# print(list_planets_2)
# a = list_planets_2.index(max(list_planets_2))
#
#
#
# print('максимальная площадь элипса', max(list_planets_2),'index' ,  list_planets_2.index(max(list_planets_2)))
#



# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


# size = int(input('Input size '))
# list_1 = [random.randint(0,10) for _ in range(size)]
# count = 0
# list_2 = []
# for i in range(1, len(list_1) -1):
#     if list_1[i -1] < list_1[i] > list_1[i + 1]:
#         count += 1
#         list_2.append(list_1[i])
# print(list_1)
# print(count)
# print(list_2)
#
#




# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# size = int(input('Input size '))
# list_1 = [random.randint(0,10) for _ in range(size)]
# count = 0
# pairs = []
# total = 0
# for i in list_1:
#     if i not in pairs:
#         count = list_1.count(i)
#         total += count//2
#         pairs.append(i)
# print(list_1, total)










# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#



# size = int(input('Input size '))
# list_1 = [random.randint(0,10) for _ in range(size)]
# print(list_1)
# size2 = int(input('Input size2 '))
# list_2 = [random.randint(0,10) for _ in range(size2)]
# print(list_2)
# list_3 = []
#
# for item in list_1:
#     if not item in list_2:
#             list_3.append(item)
# print(list_3)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# size = int(input('Input size '))
# list_1 = [random.randint(0,10) for _ in range(size)]
# print(list_1)
# list_2 =[]
# if len(list_1) %2==0:
#     for i in range(len(list_1)//2):
#         mult = list_1[i] * list_1[len(list_1)-i -1]
#         list_2.append(mult)
# else:
#     for i in range(len(list_1)//2+1):
#         mult = list_1[i] * list_1[len(list_1)-i -1]
#         list_2.append(mult)
# print(list_2)
#
#
#

