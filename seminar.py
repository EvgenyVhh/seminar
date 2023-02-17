#HOMEWORK

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



