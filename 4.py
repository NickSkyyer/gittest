# '''
# for num in range(5, -1, -1):
#     print(num)
# '''
# import random
#
# """
# BASE_SIZE = 8
#
# for r in range(BASE_SIZE):
#     for c in range(r + 1):
#         print('*', end='')
#     print()
# """
# '''
# import turtle as t
#
# t.hideturtle()
# t.speed(0)
# '''
# '''
# for x in range(4):
#     t.forward(100)
#     t.left(90)
# '''
# """
# for x in range(8):
#     t.forward(50)
#     t.left(45)
# """
# '''
# for x in range(10):
#     t.penup()
#     t.goto(0, -x * 10)
#     t.pendown()
#     t.circle(x * 10 + 20)
# '''
# '''
# t.bgcolor('#000')
#
# CIRCLES_COUNT = 60
# angle = 0
#
# for y in range(10):
#     for x in range(CIRCLES_COUNT):
#         random_num = int(random.random() * 256 ** 3)
#         random_color = '#' + hex(random_num)[2:].zfill(6)
#         t.color(random_color)
#         t.setheading(angle)
#         angle += 360 // CIRCLES_COUNT
#         t.circle(100)
#     angle += 1
# t.done()
# '''
# '''
# START_X = -200
# START_Y = 0
# NUM_LINES = 36
# LINE_LENGTH = 400
# ANGLE = 170
# ANIMATION_SPEED = 0
#
# t.penup()
# t.goto(START_X, START_Y)
# t.pendown()
#
# t.speed(ANIMATION_SPEED)
#
# for x in range(NUM_LINES):
#     t.forward(LINE_LENGTH)
#     t.left(ANGLE)
#
#
# t.done()
# '''
# '''
# product = 1
#
# while product < 100:
#     num = float(input('Enter number: '))
#     product = num * 10
# '''
#
# '''isAgain = True
#
# while isAgain:
#     a = float(input('Enter number #1: '))
#     b = float(input('Enter number #2: '))
#     sum = a + b
#     print('Sum:', sum)
#     isAgain = input('Continue? "y" -- Yes >>> ').lower() == 'y'
# '''
#
# '''for i in range(0, 1001, 10):
#     print(i, ', ', sep='', end='')
# print('\b' * 2)'''
#
# '''sum = 0.0
# for i in range(10):
#     num = float(input('Enter number #' + str(i + 1) + ': '))
#     sum += num
# print('Sum:', sum)'''
#
# '''sum = 0.0
# for i in range(1, 31):
#     sum += i / (31 - i)
# print(sum)
# '''
#
# '''for x in range(10):
#     for y in range(15):
#         print('#', end='')
#     print()'''
#
# '''num = float(input('Enter positive number: '))
# while num <= 0:
#     print('You enter NOT posivie number.' +
#           'Try again.')
#     print()
#     num = float(input('Enter number, greater zero: '))'''
#
# '''num = float(input('Enter number between 1 and 100: '))
#
# while not (1 <= num <= 100):
#     print('You enter NOT number in range [1..100].' +
#           'Try again.')
#     print()
#     num = float(input('Enter number >= 0 and <= 100: '))'''
#
# '''sum = 0
#
# for day in range(1, 6):
#     errors_count = int(input('Enter count of errors at day #' + str(day) + ': '))
#     sum += errors_count
#
# print('Total errors count:', sum)'''
#
# '''BURNING_CALORIES_PER_MINUTE = 4.2
#
# print('Minutes\tCalories')
# print('-' * 16)
#
# for minutes in range(10, 31, 5):
#     calories_burned = minutes * BURNING_CALORIES_PER_MINUTE
#     print(str(minutes) + '\t\t' + str(calories_burned))'''
#
# '''days = int(input('Count of days: '))
#
# sum = 0.0
# print('Day\t\tMoney')
#
# for day in range(days):
#     money = 0.01 * 2 ** day
#     sum += money
#     print(day, '\t', money)
#
# print('Sum =', format(sum, '.2f'))'''
#
# # sum = 0.0
# # num = float(input('Enter positive number (or negative to exit): '))
# #
# # while num > 0:
# #     sum += num
# #     num = float(input('Enter positive number (or negative to exit): '))
# #
# # print('Sum =', sum)
#
# '''num = int(input('Enter number >= 1: '))
# fact = 1
#
# for i in range(1, num + 1):
#     fact *= i
#
# print(fact)'''
#
# '''for y in range(7):
#     for x in range(7, y, -1):
#         print('*', end='')
#     print()'''
#
# '''for y in range(7):
#     print('#', end='')
#     for x in range(y):
#         print(' ', end='')
#     print('#')'''
#
# '''import turtle as t
#
# t.hideturtle()
# t.speed(0)
#
# SQUARES_COUNT = 100
# DIFFERANCE = 3
# START_SQUARE_WIDTH = SQUARES_COUNT * DIFFERANCE + 10
# square_width = START_SQUARE_WIDTH
#
# for x in range(SQUARES_COUNT):
#     for y in range(4):
#         t.forward(square_width)
#         t.left(90)
#     t.setheading(0)
#     t.forward(DIFFERANCE)
#     square_width -= DIFFERANCE
#
# t.done()'''
#
# '''import turtle as t
#
# t.hideturtle()
# t.speed(0)
#
# LINES_COUNT = 20
# ANGLE = 180 - 360 / LINES_COUNT
# LINE_WIDTH = 400
#
# t.penup()
# t.goto(-LINE_WIDTH // 2, 0)
# t.pendown()
#
# t.bgcolor('black')
# t.pencolor('yellow')
#
# for x in range(LINES_COUNT):
#     t.forward(LINE_WIDTH)
#     t.left(ANGLE)
#
# t.done()'''
#
# '''import turtle as t
#
# t.hideturtle()
# t.speed(0)
#
# DIFFERANCE = 10
# SIDES = 57
# side_width = 10
#
# t.setheading(90)
#
# for x in range(SIDES):
#     t.forward(side_width)
#     side_width += DIFFERANCE
#     t.left(90)
#
# t.done()'''
#
# '''import turtle as t
#
# t.hideturtle()
# t.speed(0)
#
# SIDE_WIDTH = 50
# SIDES_COUNT = 8
#
# t.write('STOP')
# t.penup()
# t.goto(-SIDE_WIDTH / 2 + 10, -SIDE_WIDTH / 2 - SIDE_WIDTH / 1.4142 + 5)
# t.pendown()
#
# for x in range(SIDES_COUNT):
#     t.forward(SIDE_WIDTH)
#     t.left(360 / SIDES_COUNT)
#
# t.done()'''
#
# '''def say_good_things():
#     print('С Добрым Утром!')
#     print('Я рад что ты программируешь.')
#     print('Ты очень быстро прогрессируешь.')
#
# say_good_things()
# print()
# print('END')'''
#
# '''input('Press Enter')
# print('Message')
# input('Press Enter')
# print('Message')'''
#
# '''def main():
#     principal = float(input('Enter principal: '))
#     rate = float(input('Enter rate per period: '))
#     periods = int(input('Enter periods count: '))
#
#     show_interest(principal, periods=periods, rate=rate)
#
#
# def show_interest(principal, rate, periods):
#     print(format(principal * rate * periods, '.2f'))
#
#
# main()'''
#
# '''import random
#
#
# def main():
#     random.seed(10)
#     print(random.randint(1, 100))
#     print(random.randint(1, 100))
#     print(random.randint(1, 100))
#     print(random.randint(1, 100))
#
#
# main()'''
#
# '''def main():
#     last, first, middle = get_FIO()
#     print(last, first, middle)
#
#
# def get_FIO():
#     first_name = input('First name: ')
#     middle_name = input('Middle name: ')
#     last_name = input('Last name: ')
#     return last_name, first_name, middle_name
#
#
# main()'''
#
# '''import math
#
#
# def main():
#     print(math.hypot(1, 1))
#     print(math.log(1024, 2))
#     print(math.sqrt(2))
#     print(math.radians(180))
#     print(math.pi)
#     print(math.e)
#     print(math.cos(math.radians(60)))
#
#
# main()'''
#
# '''import random
#
# for i in range(10):
#     print(random.randint(0, 100) + 1, end=' ')'''
#
# '''def is_prime(num):
#     if num < 2:
#         return False
#
#     from math import sqrt
#     for div in range(2, int(sqrt(num)) + 1):
#         if num % div == 0:
#             return False
#     return True
#
#
# for i in range(100):
#     if is_prime(i):
#         print(i, end=' ')'''
#
# '''def triangle(x1, y1, x2, y2, x3, y3, color):
#     import turtle as t
#     t.speed(0)
#     t.hideturtle()
#     t.pencolor(color)
#     t.fillcolor(color)
#     t.penup()
#     t.goto(x1, y1)
#     t.begin_fill()
#     t.pendown()
#     t.goto(x2, y2)
#     t.goto(x3, y3)
#     t.goto(x1, y1)
#     t.end_fill()
#     t.done()
#
#
# triangle(-100, -100, 0, 0, 100, -100, 'red')'''
#
# '''file = open(r'D:\test_txt.txt', 'w')
# for i in range(1, 11):
#     file.write(str(i) + '\n')
# file.close()
#
# file = open(r'D:\test_txt.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()'''
#
# '''file = open('data.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()'''
#
# '''import os
#
# os.remove(r'D:\bat\mmm.txt')'''
#
# '''file = ''
#
# try:
#     file = open('adsfasd.txt', 'r')
# except IOError as ioerror:
#     print(ioerror)
# except:
#     print("Some error")
# finally:
#     file.close()
#
# print("=)")'''
#
# '''file = open('1.txt', 'a')
# file.write('lalala')
# file.close()'''
#
# '''file = open('my_name.txt', 'w')
# file.write('Николай')
# file.close()'''
#
# '''file = open('my_name.txt', 'r')
# content = file.read()
# print(content)
# file.close()'''
#
# '''file = open('numbers_list.txt', 'w')
# for num in range(1, 101):
#     file.write(str(num) + '\n')
# file.close()'''
#
# '''file = open('numbers_list.txt', 'r')
# total = 0.0
# for line in file:
#     num = int(line)
#     total += num
# file.close()
#
# print(format(total, '.0f'))'''
#
# '''file = open('numbers_list.txt', 'a')
# file.close()'''
#
# '''import os
#
# ORIGINAL_FILENAME = 'students.txt'
# file_original = open(ORIGINAL_FILENAME, 'r')
# file_temp = open('temp.txt', 'w')
#
# STUDENT_NAME_TO_DELETE = 'John Perz'
# is_found = False
#
# name = file_original.readline().rstrip('\n')
#
# while name != '':
#
#     mark = int(file_original.readline())
#
#     if name != STUDENT_NAME_TO_DELETE:
#         file_temp.write(name + '\n')
#         file_temp.write(str(mark) + '\n')
#     else:
#         is_found = True
#
#     name = file_original.readline().rstrip('\n')
#
# file_original.close()
# file_temp.close()
#
# os.remove(ORIGINAL_FILENAME)
# os.rename('temp.txt', ORIGINAL_FILENAME)
#
# if is_found:
#     print('Студент', STUDENT_NAME_TO_DELETE, 'удален из файла.')'''
#
# '''import os
#
# ORIGINAL_FILENAME = 'students.txt'
# file_original = open(ORIGINAL_FILENAME, 'r')
# file_temp = open('temp.txt', 'w')
#
# STUDENT_NAME_TO_CHANGE_MARK = 'Julia Mulan'
# NEW_MARK = 100
# is_found = False
#
# name = file_original.readline().rstrip('\n')
#
# while name != '':
#
#     mark = int(file_original.readline())
#
#     if name != STUDENT_NAME_TO_CHANGE_MARK:
#         file_temp.write(name + '\n')
#         file_temp.write(str(mark) + '\n')
#     else:
#         is_found = True
#         file_temp.write(name + '\n')
#         file_temp.write(str(NEW_MARK) + '\n')
#
#     name = file_original.readline().rstrip('\n')
#
# file_original.close()
# file_temp.close()
#
# os.remove(ORIGINAL_FILENAME)
# os.rename('temp.txt', ORIGINAL_FILENAME)
#
# if is_found:
#     print('Студент', STUDENT_NAME_TO_CHANGE_MARK, 'изменил свою оценку на', NEW_MARK)'''
#
# '''file = open('numbers_list.txt', 'r')
# LINES_TO_SHOW = 5
# for i in range(LINES_TO_SHOW):
#     line = file.readline()
#     if line != '':
#         print(line, end='')
#     else:
#         break
# file.close()'''
#
# '''file = open('numbers_list.txt', 'r')
# line_number = 0
# for line in file:
#     # print(format(line_number, '3d') + ': ' + line, end='')
#     line_number += 1
# print(line_number)
# file.close()'''
#
# '''import random
# FILE_NAME = 'random_numbers.txt'
#
# count_of_numbers = int(input('Enter count of random numbers to save: '))
# file = open(FILE_NAME, 'w')
# for x in range(count_of_numbers):
#     file.write(str(random.randint(1, 500)) + '\n')
# file.close()'''
#
# '''FILE_NAME = 'random_numbers.txt'
#
# try:
#     file = open(FILE_NAME, 'r')
#     total = 0
#     count = 0
#     for line in file:
#         print(line, end='')
#         total += int(line)
#         count += 1
#     file.close()
#     avg = total / count
#
# except ValueError:
#     print('Ошибка чтения данных. Это должны быть целые числа.')
# except IOError:
#     print('Ошибка чтения файла. ' +
#           'Возможно ошибка в имени файла или другая программа занята файлом.')
# except ZeroDivisionError:
#     print('Файл пуст')
# else:
#     print()
#     print('-' * 30)
#     print()
#     print('Sum:', total)
#     print('Count:', count)
#     print('Avg:', format(avg, '.2f'))'''
#
# '''FILE_NAME = 'golf_players_scores.txt'
# players_count = int(input('Enter count of players: '))
#
# file = open(FILE_NAME, 'w')
# for i in range(1, players_count + 1):
#     print('Player # ' + str(i))
#     name = input('Name: ')
#     score = int(input('Score: '))
#     print()
#     file.write(name + '\n')
#     file.write(str(score) + '\n')
# file.close()'''
#
# # FILE_NAME = 'golf_players_scores.txt'
#
# '''file = open(FILE_NAME, 'a')
# for i in range(1, players_count + 1):
#     print('Player # ' + str(i))
#     name = input('Name: ')
#     score = int(input('Score: '))
#     print()
#     file.write(name + '\n')
#     file.write(str(score) + '\n')
# file.close()'''
#
# '''def set_player_score(player_name, player_score, file_name='golf_players_scores.txt'):
#     import os
#
#     try:
#         file_original = open(file_name, 'r')
#         file_temp = open('temp.txt', 'w')
#
#         is_found = False
#         name = file_original.readline().rstrip('\n')
#
#         while name != '':
#
#             score = int(file_original.readline())
#
#             if name != player_name:
#                 file_temp.write(name + '\n')
#                 file_temp.write(str(score) + '\n')
#             else:
#                 is_found = True
#                 file_temp.write(name + '\n')
#                 file_temp.write(str(player_score) + '\n')
#
#             name = file_original.readline().rstrip('\n')
#
#         if is_found:
#             print('Для игрока', player_name, 'обновлено число очков на', player_score)
#         else:
#             file_temp.write(player_name + '\n')
#             file_temp.write(str(player_score) + '\n')
#             print('Добавлен игрок ' + player_name + '. Число очков установлено на', player_score)
#
#         file_original.close()
#         file_temp.close()
#
#         os.remove(file_name)
#         os.rename('temp.txt', file_name)
#
#     except IOError:
#         print('Файл с таким именем или не существует или занят другой программой.')
#     except ValueError:
#         print('Файл содержит ошибки.')
#     except Exception as err:
#         print('Произошла ошибка. Текст ошибки:')
#         print(err)
#
#
# def show_players_scores(file_name='golf_players_scores.txt'):
#     try:
#         file = open(file_name, 'r')
#
#         print(' ' * 5 + 'Players')
#         print('-'*15)
#         name = file.readline().rstrip('\n')
#
#         while name != '':
#             score = int(file.readline())
#             print(name + '\t' + str(score))
#             name = file.readline().rstrip('\n')
#
#         file.close()
#
#
#     except IOError:
#         print('Файл с таким именем или не существует или занят другой программой.')
#     except ValueError:
#         print('Файл содержит ошибки.')
#     except Exception as err:
#         print('Произошла ошибка. Текст ошибки:')
#         print(err)
#
#
# def main():
#     # set_player_score('Ivan Ivanov', 55)
#     show_players_scores()
#
#
# main()'''
#
# """def create_personal_web_page():
#     name = input('Enter your name: ')
#     text = input('Enter text: ')
#
#     file = open('index.html', 'w')
#     file.write('''<html>
# <head>
# </head>
# <body>
#     <center>
#     <h1>''' + name + '''</h1>
#     <hr />''' + text + '''
#     <hr />
# </body>
# </html>
# ''')
#     file.close()
#
#
# def main():
#     create_personal_web_page()
#
#
# main()"""
#
# # names = ['John', 'Nick']
# # print(names)
#
# # even_numbs = list(range(2, 11, 2))
# # print(even_numbs)
#
# # numbers = [0] * 5
# # print(numbers)
#
# # numbers = [10, 20, 30] * 3
# # print(numbers)
#
# # numbers = [2, 3, 5, 7, 11, 13]
# #
# # print(len(numbers))
#
# # print(numbers[-10])
#
# # for n in numbers:
# #     print(n)
#
# # list1 = [1, 2, 3]
# # list2 = [4, 5]
# # list1 += list2
# # print(list1)
# # print(list1[1:])
#
# # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(list1[1::2])
# # print(list1[:1])
#
# '''names = ['John', 'James', 'James']
# if 'Nick' in names:
#     print('You are winner, Nick!')
# else:
#     print('Sorry, Nick. You have not win yet. Try soon again.')'''
#
# '''names = ['John', 'James', 'James']
# print(names)
# remove_name = 'James'
# while remove_name in names:
#     names.remove(remove_name)
# print(names)'''
#
# # import random
# # LIST_LEN = 10
# # numbers = []
# # for i in range(LIST_LEN):
# #     numbers.append(random.randrange(1, LIST_LEN + 1))
# # print(numbers)
# # numbers.sort()
# # print(numbers)
# # numbers.reverse()
# # print(numbers)
#
# # names = ['Anna', 'John', 'Nick']
# '''name_to_change = input('Enter name to change: ')
# try:
#     index = names.index(name_to_change)
#     names[index] = input('Enter new name: ')
#     print(names)
# except ValueError:
#     print(name_to_change, 'is not in list.')'''
#
# # print(names)
# # names.insert(len(names), 'Mark')
# # print(names)
#
# '''numbers = [1, 2, 3, 4, 5]'''
# '''print(numbers)
# del numbers[3]
# print(numbers)
# print('Min:', min(numbers))
# print('Max:', max(numbers))'''
# """print(numbers)
# numbers.sort(reverse=True)
# print(numbers)"""
#
# '''def list_sum(numbers_list):
#     total = 0.0
#     for number in numbers_list:
#         total += number
#     return total
#
#
# def main():
#     numbers = [1] * 7
#     print(list_sum(numbers))
#
#
# main()'''
#
# '''def get_list():
#     numbers = []
#     again = 'y'
#     while again == 'y':
#         value = int(input('Enter integer value: '))
#         numbers.append(value)
#         again = input("Enter 'y' for continue of other character to exit: ")
#     return numbers
#
#
# def main():
#     numbers = get_list()
#     print(numbers)
#
#
# main()'''
#
# '''def main():
#     import random
#     ROWS = 3
#     COLS = 4
#     values = [[0] * COLS] * ROWS
#     for r in range(ROWS):
#         for c in range(COLS):
#             values[r][c] = random.randint(1, 100)
#
#     print(values)
#
#
# main()'''
#
# '''def main():
#     numbers = [[1, 2], [10, 20], [100, 200], [1000, 2000]]
#     for r in range(4):
#         for c in range(2):
#             print(format(numbers[r][c], '5d'), end='')
#         print()
#
#
# main()'''
#
# '''def main():
#     my_list = [1, 2, 3]
#     my_tuple = tuple(my_list)
#     print(my_tuple)
#     my_list = list(my_tuple)
#     print(my_list)
#
#
# main()'''
#
# """import matplotlib.pyplot as plt
#
# x_coords = [0, 1, 2, 3, 4]
# y_coords = [0, 3, 1, 5, 2]
#
# plt.plot(x_coords, y_coords, marker='o')
# plt.title('Sample Data')
# plt.xlabel('Year')
# plt.ylabel('Sales')
# plt.xlim(xmin=-1, xmax=5)
# plt.ylim(ymin=-1, ymax=6)
# plt.xticks([0, 1, 2, 3, 4],
#            ['2016', '2017', '2018', '2019', '2020'])
# plt.yticks([0, 1, 2, 3, 4, 5],
#            ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
# plt.grid()
# plt.show()"""
#
# """import matplotlib.pyplot as plt
#
# bars_centers = (2.5, 12.5, 22.5, 32.5, 42.5)
# heights = (100, 200, 300, 400, 500)
# plt.bar(bars_centers, heights, width=5, color=('r', 'g', 'b', 'y', 'k'))
# plt.title('Sales by Year')
# plt.xlabel('Year')
# plt.ylabel('Sales')
# plt.xticks([2.5, 12.5, 22.5, 32.5, 42.5],
#            ['2016', '2017', '2018', '2019', '2020'])
# plt.yticks([0, 100, 200, 300, 400, 500],
#            ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
# plt.show()"""
#
# '''import matplotlib.pyplot as plt
#
# values = (100, 400, 300, 600)
# slice_labels = ('1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr')
# plt.pie(values, labels=slice_labels, colors=('r', 'g', 'b', 'c'))
# plt.title('Sales by Quarter')
# plt.show()'''
#
# '''mylist = []
# mylist.append('Labrador')
# print(mylist.index('Labrador'))'''
#
# # print(list(range(1, 101)))
#
# '''names = ['Name1', 'Name2']
# for name in names:
#     print(name)'''
#
# '''import random
#
# scores = [0] * 10
# index = 0
# while index < 10:
#     scores[index] = random.randint(0, 100)
#     index += 1
# print(scores)
# scores.sort()
# print(scores)
# scores.reverse()
# print(scores)
# print(max(scores))
# print(scores[0])'''
#
# '''def get_list_total(lst):
#     total = .0
#     for n in lst:
#         total += n
#     return total
#
#
# print(get_list_total([1, 2, 3]))'''
#
# '''NAME_TO_FIND = 'Ruby'
# names = ['Ruby', 'Ron', 'Ray']
# if NAME_TO_FIND in names:
#     print('Hello ' + NAME_TO_FIND)
# else:
#     print('No ' + NAME_TO_FIND)'''
#
# ROWS = 5
# COLS = 3
#
# # numbers = [[0] * 3] * 5
# '''numbers = [[0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0]]
#
# for r in range(ROWS):
#     for c in range(COLS):
#         numbers[r][c] = r * COLS + c + 1
# """int(input('Enter [' + str(r) + '][' + str(c) + ']: '))"""
#
# for r in range(ROWS):
#     for c in range(COLS):
#         print(format(numbers[r][c], '3d'), end=' ')
#     print()'''
#
# '''numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
#
# def get_valid_numbers(numbers, START, END):
#     valid_numbers = []
#     for number in numbers:
#         if number in range(START, END + 1):
#             valid_numbers.append(number)
#     return valid_numbers
#
# valid_numbers = get_valid_numbers(numbers, 0, 100)
# print(valid_numbers)'''
#
# '''import random
#
# LOTTERY_NUMBER_LENGTH = 7
# lottery_number = [0] * LOTTERY_NUMBER_LENGTH
# for i in range(LOTTERY_NUMBER_LENGTH):
#     lottery_number[i] = random.randint(0, 9)
# for digit in lottery_number:
#     print(digit, end=' ')'''
#
# '''FILE_NAME = 'charge_accounts.txt'
# file = open(FILE_NAME, 'r')
# charge_accounts = []
# for line in file:
#     number = int(line)
#     charge_accounts.append(number)
# file.close()
#
# print(charge_accounts)
#
# user_number = int(input('Enter a charge account number: '))
# if user_number in charge_accounts:
#     print('The number is valid.')
# else:
#     print('The number is invalid.')'''
#
# '''def roll(number_of_throws):
#     import random
#     throws = []
#     for throw in range(number_of_throws):
#         throws.append(random.randint(1, 6))
#     throws.sort()
#     return throws
#
#
# def main():
#     print(roll(3))
#
#
# main()'''
#
# '''QUESTIONS_COUNT = 20
#
#
# def get_student_answers():
#     student_answers = ['-'] * 20
#     for i in range(QUESTIONS_COUNT):
#         student_answers[i] = input('Enter your answer (a, b, c, d) #' + str(i + 1) + ': ')
#     return student_answers
#
#
# def save_student_answers(student_answers):
#     file = open('student_answers.txt', 'w')
#     for student_answer in student_answers:
#         file.write(student_answer + '\n')
#     file.close()
#
#
# def check_student_answers(CORRECT_ANSWERS, student_answers):
#     score = 0
#     index = 0
#     uncorrect_answers = []
#     while index < QUESTIONS_COUNT:
#         if student_answers[index] == CORRECT_ANSWERS[index]:
#             score += 1
#         else:
#             uncorrect_answers.append(index + 1)
#         index += 1
#     print('Score (count of correct answers):', score)
#     print('Count of wrong answers:', QUESTIONS_COUNT - score)
#     MIN_CORRECT_ANSWERS_COUNT_TO_PASS = 15
#     if score >= MIN_CORRECT_ANSWERS_COUNT_TO_PASS:
#         print('Congrats! You have passed the exam.')
#     else:
#         print("Oops... You haven't passed the exam. Try again.")
#
#     if len(uncorrect_answers) > 0:
#         print('\tUncorrect answers numbers:')
#         print(uncorrect_answers)
#
#
# def main():
#     CORRECT_ANSWERS = ['a', 'c', 'a', 'a',
#                        'd', 'b', 'c', 'a',
#                        'c', 'b', 'a', 'd',
#                        'c', 'a', 'd', 'c',
#                        'b', 'b', 'd', 'a']
#     student_answers = get_student_answers()
#     save_student_answers(student_answers)
#     check_student_answers(CORRECT_ANSWERS, student_answers)
#
#
# main()
# '''
#
# '''def get_file_lines(file_name):
#     file = open(file_name, 'r')
#     lines = []
#     line = file.readline().rstrip('\n')
#     while line != '':
#         lines.append(line)
#         line = file.readline().rstrip('\n')
#     file.close()
#     return lines
#
#
# def is_popular_name(name, popular_names):
#     return name in popular_names
#
#
# def main():
#     boy_names = get_file_lines('BoyNames.txt')
#     girl_names = get_file_lines('GirlNames.txt')
#
#     boy_name = input('Enter boy\'s name: ')
#     if is_popular_name(boy_name, boy_names):
#         print('Name', boy_name, ' is one of the most popular boy\'s names in USA (TOP 200).')
#     else:
#         print('Name', boy_name, ' is NOT one of the most popular boy\'s names in USA (TOP 200).')
#
#     girl_name = input('Enter girl\'s name: ')
#     if is_popular_name(girl_name, girl_names):
#         print('Name', girl_name, ' is one of the most popular boy\'s names in USA (TOP 200).')
#     else:
#         print('Name', girl_name, ' is one of the most popular boy\'s names in USA (TOP 200).')
#
#
# main()'''
#
# """def get_file_numbers(file_name):
#     file = open(file_name, 'r')
#     lines = []
#     line = file.readline().rstrip('\n')
#     while line != '':
#         lines.append(int(line))
#         line = file.readline().rstrip('\n')
#     file.close()
#     return lines
#
#
# def add_lists_elements(list1, list2):
#     shorter_list = min(len(list1), len(list2))
#     result = [0] * shorter_list
#     for i in range(len(result)):
#         result[i] = list1[i] + list2[i]
#     return result
#
#
# def main():
#     populations = get_file_numbers('USPopulation.txt')
#     population_increases = []
#     i = 0
#     while i < len(populations) - 1:
#         increase = populations[i + 1] - populations[i]
#         population_increases.append(increase)
#         i += 1
#     START_YEAR = 1950
#     END_YEAR = 1990
#     years = list(range(START_YEAR, END_YEAR + 1))
#
#     avg_annual_population_change = (populations[-1] - populations[0]) / len(years)
#     print('The average annual change in population during the time period:', avg_annual_population_change)
#     print('The year with the greatest increase in population during the time period:', max(population_increases))
#     print('The year with the smallest increase in population during the time period:', min(population_increases))
#     import matplotlib.pyplot as plt
#     # plt.plot(years[1:], population_increases)
#     # plt.show()
# '''
#     for i in range(1, 11):
#         population_parts = [int(p * 0.01 * i) for p in populations]
#         population_parts_plus_increases = add_lists_elements(population_parts[1:], population_increases)
#         plt.plot(years[1:], population_parts_plus_increases)
#         plt.show()
# '''
#
#
# main()"""
#
# """def get_file_lines(file_name):
#     file = open(file_name, 'r')
#     lines = []
#     line = file.readline().rstrip('\n')
#     while line != '':
#         lines.append(line)
#         line = file.readline().rstrip('\n')
#     file.close()
#     return lines
#
#
# def main():
#     winners_teams = get_file_lines('WorldSeriesWinners.txt')
#     print(winners_teams)
#     find_team = input('Enter name of a team: ')
#     count = 0
#     for team in winners_teams:
#         if team == find_team:
#             count += 1
#     print('The team "' + find_team + '" had win ' + str(count) + ' time(s).')
#
#
# main()"""
#
# """def is_Lo_Shu_Magic_Square(lst):
#     ROWS = 3
#     COLS = 3
#     main_sum = 0
#     for c in range(COLS):
#         main_sum += lst[0][c]
#
#     for r in range(1, ROWS):
#         sum = 0
#         for c in range(COLS):
#             sum += lst[r][c]
#         if main_sum != sum:
#             return False
#
#     for c in range(COLS):
#         sum = 0
#         for r in range(ROWS):
#             sum += lst[r][c]
#         if main_sum != sum:
#             return False
#
#     sum = 0
#     for r in range(ROWS):
#         sum += lst[r][r]
#     if main_sum != sum:
#         return False
#
#     sum = 0
#     for r in range(ROWS - 1, -1, -1):
#         sum += lst[r][r]
#     if main_sum != sum:
#         return False
#     return True
#
#
# def main():
#     Lo_Shu_Magic_Square = [[4, 9, 2],
#                            [3, 5, 7],
#                            [8, 1, 6]]
#
#     print(is_Lo_Shu_Magic_Square(Lo_Shu_Magic_Square))
#
#
# main()"""
#
# '''def get_file_lines(file_name):
#     lines = []
#
#     try:
#         file = open(file_name, 'r')
#         line = file.readline().rstrip('\n')
#         while line != '':
#             lines.append(line)
#             line = file.readline().rstrip('\n')
#         file.close()
#     except IOError:
#         print('Ошибка чтения файла. ' +
#               'Или ошибка в имени файла (файл с таким именем не найден), ' +
#               'или файл не может быть открыт.')
#
#     return lines
#
#
# def show_lines_with_numbers(lines):
#     n = 1
#     for line in lines:
#         print(n, line)
#         n += 1
#
#
# def main():
#     file_name = input('Enter file name to read its lines: ')
#     lines = get_file_lines(file_name=file_name)
#     if lines:
#         show_lines_with_numbers(lines)
#         try:
#             line_number = int(input('Enter line number to show: '))
#             if 1 > line_number or line_number > len(lines):
#                 raise IndexError
#         except ValueError:
#             print('Введите целое число')
#         except IndexError:
#             print('Введите целое число от 1 до', len(lines))
#         else:
#             print(lines[line_number - 1])
#     pass
#
#
# main()'''
#
# '''def get_file_lines(file_name):
#     lines = []
#
#     try:
#         file = open(file_name, 'r')
#         line = file.readline().rstrip('\n')
#         while line != '':
#             lines.append(line)
#             line = file.readline().rstrip('\n')
#         file.close()
#     except IOError:
#         print('Ошибка чтения файла. ' +
#               'Или ошибка в имени файла (файл с таким именем не найден), ' +
#               'или файл не может быть открыт.')
#
#     return lines
#
#
# def main():
#     responses = get_file_lines('8_ball_responses.txt')
#     question = input('Enter your question: ')
#     import random
#     print('Answer:', responses[random.randrange(len(responses))])
#
#
# main()'''
#
# '''def get_file_numbers(file_name):
#     numbers = []
#
#     try:
#         file = open(file_name, 'r')
#         line = file.readline().rstrip('\n')
#         while line != '':
#             numbers.append(float(line))
#             line = file.readline().rstrip('\n')
#         file.close()
#     except IOError:
#         print('Ошибка чтения файла. ' +
#               'Или ошибка в имени файла (файл с таким именем не найден), ' +
#               'или файл не может быть открыт.')
#
#     return numbers
#
#
# def main():
#     expenses = get_file_numbers('expenses.txt')
#     import matplotlib.pyplot as plt
#     plt.pie(expenses, labels=['Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc'])
#     plt.show()
#
#
# main()'''
#
# '''def get_file_lines(file_name):
#     lines = []
#
#     try:
#         file = open(file_name, 'r')
#         line = file.readline().rstrip('\n')
#         while line != '':
#             lines.append(line)
#             line = file.readline().rstrip('\n')
#         file.close()
#     except IOError:
#         print('Ошибка чтения файла. ' +
#               'Или ошибка в имени файла (файл с таким именем не найден), ' +
#               'или файл не может быть открыт.')
#
#     return lines
#
#
# def main():
#     lines = get_file_lines('GasPrices.txt')
#     PRICES_COUNT = len(lines)
#     dates = [''] * PRICES_COUNT
#     gas_prices = [0.0] * PRICES_COUNT
#     for i in range(PRICES_COUNT):
#         dates[i] = lines[i][:5]  # [:10]
#         gas_prices[i] = float(lines[i][11:])
#     import matplotlib.pyplot as plt
#     px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
#     plt.subplots(figsize=(6000*px, 2000*px))
#     DATA_SIZE = 100
#     plt.plot(dates[:DATA_SIZE], gas_prices[:DATA_SIZE])
#     plt.show()
#
#
# main()'''
#
# """name = 'Nick'
# and_ = ' and '
# name2 = 'Johanna'
# name += and_ + name2
# print(name)
# # for c in name:
# #     print(c)
# #     c = 'X'
# #     print(c)
# #     print(name)
# # print(name)
#
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(letters[0:26:2])
# print(letters[::2])
#
# if 'CD' in letters:
#     print('CD -- is a part of a sequence of the English alphabet.')
#
# print('1991'.isdigit())
# print('1991'.isdigit())"""
#
# '''str = '\t'
#
# if str.isalnum():
#     print('alphabetic letters + digits')
# if str.isalpha():
#     print('alphabetic letters only')
# if str.isdigit():
#     print('digits only')
# if str.islower():
#     print('lower case only')
# if str.isupper():
#     print('upper case only')
# if str.isspace():
#     print('space(s) only')'''
#
# """str1 = '  абВГ   '
# str2 = '--абВГ---'
# print('\tstr1')
# print('lower:' + str1.lower())
# print('upper:' + str1.upper())
# print('upper and strip:' + str1.strip().upper())
#
# print('\n\tstr2')
# print('lower:' + str2.lower())
# print('upper:' + str2.upper())
# print('upper and strip:' + str2.strip('-').upper())
# print('upper and lstrip:' + str2.lstrip('-').upper())"""
#
# '''file_name = input('Enter file name: ')
# if file_name.endswith('.txt'):
#     print('It is a text file')
# elif file_name.endswith('.mp3'):
#     print('It is audio file')'''
#
# '''text = 'Some long boring text.'
# position = text.lower().find('some')
# print(position)
# print(text)
# print(text.replace('boring', 'interesting'))
#
# for count in range(1, 10):
#     print('Z' * count)
#
# for count in range(8, 0, -1):
#     print('Z' * count)'''
#
# '''text = 'Some long boring text.'
# print(text)
# words = text.replace('.', '').split()
# print(words)
# print('22.12.1991'.split('.'))'''
#
# """mystring = 'dog'
# if 'd' in mystring:
#     print('Letter "d" is in string variable \'mystring\'')"""
#
# # big = 'ABC'
# # little = big.lower()
#
# """ch = '1'
# if ch.isnumeric():
#     print('Digit')
# else:
#     print('No digit.')"""
#
# """answer = 'R'
# while answer.upper() == 'R':
#     answer = input('Do you want to repeat the program or quit? >>> ')
#     if answer.upper() == 'Q':
#         break
#     elif answer.upper() != 'R':
#         print('Unknown answer')
#         answer = 'R'"""
#
# """mystring = 'AcAcAc'
# count = 0
# for ch in mystring:
#     if ch.isupper():
#         count += 1
# print(count)"""
#
# '''days = 'Monday Tuesday Wednesday'
# print(days.split())
# values = 'one$two$three$four'
# print(values.split('$'))
# print('12f'.isdigit())'''
#
# """mystr = 'abracadabra'
# print(mystr[6:9])"""
#
# """mystring = 'One two three .'
# count = 0
# for ch in mystring:
#     if ch == ' ':
#         count += 1
# print(count)"""
#
# """mystring = 'One 1 two 2 three .'
# count = 0
# for ch in mystring:
#     if ch.isalnum():
#         count += 1
# print(count)"""
#
# '''mystring = 'One 1 two 2 three .'
# count = 0
# for ch in mystring:
#     if ch.islower():
#         count += 1
# print(count)'''
#
# '''def is_https(str):
#     return str.startswith('https')
#
# link = 'https://google.com'
# if is_https(link):
#     print('It\'s a safety link.')
# else:
#     print('It\' NOT a safety link. Be careful.')'''
#
# '''str = 'Total control is my main dream. I am trying to achieve this dream as soon as possible.'
# str2 = ''
# for ch in str:
#     if ch != 't':
#         str2 += ch
#     else:
#         str2 += 'T'
# print(str2)'''
#
# '''def my_reverse(str):
#     str2 = ''
#     for i in range(len(str) - 1, -1, -1):
#         str2 += str[i]
#     return str2
#
#
# print(my_reverse('abcdef'))'''
#
# '''mystring = '123456789'
# print(mystring[:3])
# print(mystring[-3:])'''
#
# '''levels = 'Beginner, Average, Advanced, Expert'
# print(levels.split(', '))'''
#
# '''full_name = input('Enter your full name (like John Smith): ')
# full_name_parts = full_name.split()
# first_name = full_name_parts[0][0].upper() + full_name_parts[0][1:]
# second_name = full_name_parts[1][0].upper() + full_name_parts[1][1:]
# initials = first_name[0] + '.' + second_name[0] + '.'
# name_in_address_book = first_name + ' ' + second_name.upper()
# username = first_name[0].lower() + second_name.lower()
# print('Initials:', initials)
# print('Name in address book:', name_in_address_book)
# print('Username:', username)'''
#
# '''numbers = input('Enter digits without separating: ')
# total = 0
# for ch in numbers:
#     number = int(ch)
#     total += number
# print(total)'''
#
# '''months = ['January', 'February', 'March',
#           'April', 'May', 'June', 'July',
#           'August', 'September', 'October',
#           'November', 'December']
#
# date = input('Enter date in format mm/dd/yyyy: ').strip()
# date = date.split('/')
# month = int(date[0])
# month = months[month - 1]
# day = date[1]
# year = date[2]
# print(month, day + ', ' + year)'''
#
# '''def get_morse_code(str):
#     CHARS = (' ', '0', '1', '2', '3', '4', '5',
#              'A', 'K', 'U', 'B', 'L', 'V', 'C', 'M', 'W', 'D',
#              'N', 'X', 'E', 'O', 'Y', 'F', 'P', 'Z',
#              '6', 'G', 'Q', ',', '7', 'H', 'R', '.', '8', 'I', 'S', '?', '9', 'J', 'T')
#     CODE = (' ', '–––––', '.––––', '..–––', '...––', '....–', '.....',
#             '.–', '–.–', '..–', '–...', '.–..', '...–', '–.–.',
#             '––', '.––', '–..', '–.', '–..–', '.', '–––', '–.–', '..–.',
#             '.––.', '––..', '–....', '––.', '––.–', '––..––', '––...', '....', '.–.',
#             '.–.–.–', '–––..', '..', '...', '..––..',
#             '––––.', '.–––', '–')
#     code = ''
#     for ch in str:
#         index = CHARS.index(ch)
#         if index != -1:
#             code += CODE[index]
#     return code
#
#
# print(get_morse_code('AB'))'''
#
# '''A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9'''
#
# '''LETTERS = ('ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
#
# telephone_number_with_letters = '555-GET-FOOD'
# telephone_number = ''
# for ch in telephone_number_with_letters:
#     if not ch.isalpha():
#         telephone_number += ch
#     else:
#         ch = ch.upper()
#         for s in LETTERS:
#             try:
#                 s.index(ch)
#             except ValueError:
#                 pass
#             else:
#                 telephone_number += str(LETTERS.index(s) + 2)
# print(telephone_number)'''
#
# '''def get_file_lines(file_name):
#     lines = []
#
#     try:
#         file = open(file_name, 'r')
#         line = file.readline().rstrip('\n')
#         while line != '':
#             lines.append(line)
#             line = file.readline().rstrip('\n')
#         file.close()
#     except IOError:
#         print('Ошибка чтения файла. ' +
#               'Или ошибка в имени файла (файл с таким именем не найден), ' +
#               'или файл не может быть открыт.')
#
#     return lines'''
#
# '''lines = get_file_lines('text.txt')
# total = 0
# for line in lines:
#     line2 = ''.join([ch for ch in line if ch in [' '] or ch.isalpha()])
#     line2 = line2.replace('  ', ' ')
#     total += len(line2.split())
# avg = total / len(lines)
# print('Avg count of words in sentence:', format(avg, '.1f'))'''
#
# '''file = open('text.txt', 'r')
# text = file.read()
# file.close()
#
# uppercase_letters_count = 0
# lowercase_letters_count = 0
# digits_count = 0
# whitespace_characters_count = 0
# dots = 0
#
# for ch in text:
#     if ch.isupper():
#         uppercase_letters_count += 1
#     elif ch.islower():
#         lowercase_letters_count += 1
#     elif ch.isdigit():
#         digits_count += 1
#     elif ch.isspace():
#         whitespace_characters_count += 1
#     elif ch == '.':
#         dots += 1
#
# print(uppercase_letters_count)
# print(lowercase_letters_count)
# print(digits_count)
# print(whitespace_characters_count)
# print(dots)'''
#
# '''def capitalize_sentence(str):
#     sentence_end_chars = ('.', '!', '?')
#     str2 = ''
#     # True, because every sentence
#     # starts with uppercase character
#     is_end_char_appear = True
#     for ch in str:
#         if ch in sentence_end_chars:
#             is_end_char_appear = True
#             str2 += ch
#         elif is_end_char_appear:
#             if ch.isalpha():
#                 str2 += ch.upper()
#                 is_end_char_appear = False
#             else:
#                 str2 += ch
#         else:
#             str2 += ch
#     return str2
#
#
# def main():
#     str = input('Enter sentence: ')
#     print(capitalize_sentence(str))
#     pass
#
#
# main()'''
#
# '''def get_most_frequent_character(str):
#     chars = []
#     # add unique chars to chars list
#     for ch in str:
#         if ch not in chars:
#             chars.append(ch)
#     chars_counts = [0] * len(chars)
#     for ch in str:
#         i = chars.index(ch)
#         chars_counts[i] += 1
#
#     index = chars_counts.index(max(chars_counts))
#     return chars[index]
#
#
# def main():
#     str = input('Enter string: ')
#     print('Most frequent character:', get_most_frequent_character(str))
#
#
# main()'''
#
# '''def main():
#     str = 'StopAndSmellTheRoses'
#     str2 = ''
#     index = 0
#     while index < len(str):
#         ch = str[index]
#         if ch.isupper() and index != 0:
#             str2 += ' ' + ch.lower()
#         else:
#             str2 += ch
#         index += 1
#     print(str2)
#
#
# main()'''
#
# '''def get_pig_latin_word(word):
#     word2 = word[1:] + word[0] + 'AY'
#     return word2
#
#
# def main():
#     str = 'I SLEPT MOST OF THE NIGHT'
#     str_res = 'IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY'
#     words = str.split()
#
#     i = 0
#     while i < len(words):
#         words[i] = get_pig_latin_word(words[i])
#         i += 1
#
#     str2 = ' '.join(words)
#     print(str2)
#
#
# main()'''
#
# '''def get_numbers_from_file(file_name):
#     file = open(file_name, 'r')
#     numbers = []
#     for line in file:
#         strings_of_numbers = line.rstrip().split()
#         for number in strings_of_numbers:
#             numbers.append(number)
#     file.close()
#     return numbers
#
#
# def get_most_common_numbers(numbers, numbers_count, count_of_numbers_to_get):
#     most_common_numbers = []
#     numbers2 = numbers[:]
#     numbers_count2 = numbers_count[:]
#     for i in range(count_of_numbers_to_get):
#         max_count = max(numbers_count2)
#         index_max = numbers_count2.index(max_count)
#         most_common_value = numbers2[index_max]
#         most_common_numbers.append(most_common_value)
#         del numbers2[index_max]
#         del numbers_count2[index_max]
#
#     return most_common_numbers
#
#
# def get_least_common_numbers(numbers, numbers_count, count_of_numbers_to_get):
#     least_common_numbers = []
#     numbers2 = numbers[:]
#     numbers_count2 = numbers_count[:]
#     for i in range(count_of_numbers_to_get):
#         min_count = min(numbers_count2)
#         index_min = numbers_count2.index(min_count)
#         min_common_value = numbers2[index_min]
#         least_common_numbers.append(min_common_value)
#         del numbers2[index_min]
#         del numbers_count2[index_min]
#
#     return least_common_numbers
#
#
# def get_number_frequency(number, numbers):
#     count = 0
#     numbers2 = numbers[:]
#     while number in numbers2:
#         count += 1
#         numbers2.remove(number)
#     return count / len(numbers)
#
#
# def main():
#     numbers = get_numbers_from_file('pbnumbers.txt')
#     unique_numbers = []
#     for n in range(len(numbers)):
#         if numbers[n] not in unique_numbers:
#             unique_numbers.append(numbers[n])
#     unique_numbers.sort()
#     numbers_count = [0] * len(unique_numbers)
#     for n in range(len(numbers)):
#         index = int(numbers[n]) - 1
#         numbers_count[index] += 1
#
#     print(numbers_count)
#     print(unique_numbers)
#     print('10 most common numbers:', ', '.join(get_most_common_numbers(unique_numbers, numbers_count, 10)))
#     print('10 least common numbers:', ', '.join(get_least_common_numbers(unique_numbers, numbers_count, 10)))
#     print('\tFrequency of numbers:')
#     print()
#     for num in unique_numbers:
#         print(num + ': ' + format(get_number_frequency(num, numbers), '.2%'))
#
#
# main()'''
#
# '''def get_file_lines(file_name):
#     file = open(file_name, 'r')
#     lines = []
#     for line in file:
#         lines.append(line.rstrip())
#     return lines
#
#
# def get_unique_years(lines):
#     unique_years = []
#     for line in lines:
#         year = int(line[6:10])
#         if year not in unique_years:
#             unique_years.append(year)
#     return unique_years
#
#
# def get_avg_gas_price_in_year(lines, year):
#     sum = 0
#     count = 0
#     year = str(year)
#     for line in lines:
#         if line[6:10] == year:
#             sum += float(line[11:])
#             count += 1
#     return sum / count
#
#
# def get_unique_months(lines):
#     unique_months = []
#     for line in lines:
#         month = line[:2]
#         if month not in unique_months:
#             unique_months.append(month)
#     unique_months.sort()
#     return unique_months
#
#
# def get_avg_gas_price_in_month(lines, month):
#     sum = 0
#     count = 0
#     month = str(month)
#     for line in lines:
#         if line[:2] == month:
#             sum += float(line[11:])
#             count += 1
#     if count != 0:
#         return sum / count
#     return 0
#
#
# def get_highest_gas_price_in_year(lines, year):
#     prices_in_year = []
#     year = str(year)
#     for line in lines:
#         if line[6:10] == year:
#             price = float(line[11:])
#             prices_in_year.append(price)
#     return max(prices_in_year)
#
#
# def get_lowest_gas_price_in_year(lines, year):
#     prices_in_year = []
#     year = str(year)
#     for line in lines:
#         if line[6:10] == year:
#             price = float(line[11:])
#             prices_in_year.append(price)
#     return min(prices_in_year)
#
#
# def save_ascending_prices_to_file():
#     lines = get_file_lines('GasPrices.txt')
#     dates = []
#     prices = []
#     for line in lines:
#         data = line.split(':')
#         dates.append(data[0])
#         prices.append(float(data[1]))
#
#     sorted_prices = []
#     sorted_dates_by_price = []
#
#     while len(dates) > 0:
#         min_price = min(prices)
#         sorted_prices.append(min_price)
#         index = prices.index(min_price)
#         del prices[index]
#         sorted_dates_by_price.append(dates[index])
#         del dates[index]
#
#     file = open('lowest_to_highest_gas_prices.txt', 'w')
#     for i in range(len(sorted_prices)):
#         file.write(sorted_dates_by_price[i] + ':' + str(sorted_prices[i]) + '\n')
#     file.close()
#
#
# def save_descending_prices_to_file():
#     lines = get_file_lines('GasPrices.txt')
#     dates = []
#     prices = []
#     for line in lines:
#         data = line.split(':')
#         dates.append(data[0])
#         prices.append(float(data[1]))
#
#     sorted_prices = []
#     sorted_dates_by_price = []
#
#     while len(dates) > 0:
#         max_price = max(prices)
#         sorted_prices.append(max_price)
#         index = prices.index(max_price)
#         del prices[index]
#         sorted_dates_by_price.append(dates[index])
#         del dates[index]
#
#     file = open('highest_to_lowest_gas_prices.txt', 'w')
#     for i in range(len(sorted_prices)):
#         file.write(sorted_dates_by_price[i] + ':' + str(sorted_prices[i]) + '\n')
#     file.close()
#
#
# def main():
#     save_descending_prices_to_file()'''
#
# # unique_years = get_unique_years(lines)
# # print('Year\tHighest gas price\tLowest gas price')
# # print()
# # for unique_year in unique_years:
# #     print(unique_year, '\t\t' + str(get_highest_gas_price_in_year(lines, unique_year)),
# #           '\t\t\t\t' + str(get_lowest_gas_price_in_year(lines, unique_year)))
#
# # unique_years = get_unique_years(lines)
# # print('Year\tAvg gas price')
# # print()
# # for unique_year in unique_years:
# #     print(unique_year, '\t' + str(get_avg_gas_price_in_year(lines, unique_year)))
#
# # unique_months = get_unique_months(lines)
# # print(unique_months)
# # print('Month\tAvg gas price')
# # print()
# # for month in unique_months:
# #     print(month, '\t' + str(get_avg_gas_price_in_month(lines, month)))
#
#
# """def get_caesar_cipher(str, shifting):
#     alphabet = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
#     # print('  '.join(alphabet))
#     # print(' '.join([format(i, '02d') for i in range(1, 27)]))
#     encrypted_str = ''
#     for ch in str:
#         if ch in alphabet:
#             index = alphabet.index(ch)
#             new_index = (index + shifting) % len(alphabet)
#             encrypted_str += alphabet[new_index]
#         else:
#             encrypted_str += ch
#     return encrypted_str
#
# def main():
#     str = 'BEWARE THE IDES OF MARCH'
#     shifting = 13
#     encrypted_str = get_caesar_cipher(str, shifting)
#     print(encrypted_str)
#     if encrypted_str == 'ORJNER GUR VQRF BS ZNEPU':
#         print('GOOD')
#     else:
#         print('BAD')
#
#
# main()"""
#
# '''phonebook = {'Nick': '066-1889-110', 'Somebody': '066-1234-567'}
# if 'Somebody2' not in phonebook:
#     phonebook['Somebody2'] = 1
#     print(phonebook['Somebody2'])
# print(phonebook)
# print(len(phonebook))
# del phonebook['Somebody']
# print(phonebook)
# print(len(phonebook))
# if 'Somebody3' in phonebook:
#     del phonebook['Somebody3']'''
#
# # print(test_scores['Nick'])
#
# # for key in test_scores:
# #     print(key, test_scores[key])
#
# # dict1 = {}
# # dict2 = dict()
# # print(type(dict1))
# # print(type(dict2))
#
# # test_scores = {'Nick': [5, 5, 5], 'John': [4, 4, 5]}
#
# # print(test_scores.values())
# # print(type(test_scores.items()))
# # print(test_scores.pop('Nicks', 'Not found'))
# # print(test_scores)
#
#
# # for k in test_scores:
# #     print(k)
# # for value in test_scores.values():
# #     print(value)
#
# # k, v = test_scores.popitem()
# # print(k)
# # print(v)
# # print(test_scores)
#
# # phone_num = test_scores.pop('Nick', 'Entry not found')
# # print(phone_num)
# # phone_num = test_scores.pop('Madonna', 'Entry not found')
# # print(phone_num)
# # print(test_scores)
#
# # for key in test_scores.keys():
# #     print(key)
#
# # for key, value in test_scores.items():
# #     print(key, value)
#
# # value = test_scores.get('Nick3', 'Entry not found')
# # print(value)
# # print(test_scores)
# # test_scores.clear()
# # print(test_scores)
#
#
# # letters = set('Hello. How are you? Where have you been?')
# # print(letters)
#
# # words = set(('one', 'two', 'three'))
# # print(words)
# # print(len(words))
# # words.add('four')
# # print(words)
# # words.add('one')
# # print(words)
# # my_dict = {'five': 5, 'six': 6}
# # words.update(my_dict.keys())
# # print(words)
# # words.remove('three')
# # print(words)
# # words.discard('four')
# # print(words)
# # words.discard('seven')
# # print(words)
# # # words.remove('seven')
# # # words.clear()
# # print(words)
# # for word in words:
# #     print(word)
# # if 'six' in words:
# #     print('Value "six" is in words set.')
# # if 'seven' not in words:
# #     print('Value "seven" is NOT in words set.')
# # print(words)
#
# # set1 = set([1, 2, 3, 4])
# # set2 = set([3, 4, 5, 6])
# # # set3 = set1.union(set2)
# # set3 = set1 | set2
# # print(set3)
# #
# # # set4 = set1.intersection(set2)
# # set4 = set1 & set2
# # print(set4)
# #
# # # set5 = set1.difference(set2)
# # set5 = set1 - set2
# # print(set5)
# #
# # # set6 = set1.symmetric_difference(set2)
# # set6 = set1 ^ set2
# # print(set6)
#
# # set1 = {1, 2, 3, 4, 5}
# # set2 = {1, 2}
# # print(set1.issuperset(set2))
# # print(set1 >= set2)
# # print(set2.issubset(set1))
# # print(set2 <= set1)
# # print(set2.issuperset(set1))
# # print(set2 >= set1)
# # print(set1.issubset(set2))
# # print(set1 <= set2)
# # set1.remove(66)
#
# '''import pickle
#
#
# def display(person):
#     print('Name:', person['name'])
#     print('Age:', person['age'])
#     print('Weight:', person['weight'])
#     print()
#
#
# def save_people(FILE_NAME):
#     output_file = open(FILE_NAME, 'wb')
#     again = 'y'
#     while again.lower() == 'y':
#         save_person(output_file)
#         again = input('Enter (y/n) to continue or exit: ')
#     output_file.close()
#
#
# def save_person(file):
#     person = {}
#     person['name'] = input('Name: ')
#     person['age'] = int(input('Age: '))
#     person['weight'] = float(input('Weight: '))
#     pickle.dump(person, file)
#
#
# def show_people(FILE_NAME):
#     input_file = open(FILE_NAME, 'rb')
#     is_eof = False
#     while not is_eof:
#         try:
#             person = pickle.load(input_file)
#             display(person)
#         except EOFError:
#             is_eof = True
#
#     input_file.close()
#
#
# def main():
#     FILE_NAME = 'people.dat'
#     save_people(FILE_NAME)
#     show_people(FILE_NAME)
#
#
# main()
# '''
#
# # dct = {'James': 100000}
# # if 'James' in dct:
# #     print(dct['James'])
# # else:
# #     print('No key "James" in dictionary.')
#
# # dct = {'Jon': 45}
# # print(dct)
# # if 'Jon' in dct:
# #     dct['John'] = dct['Jon']
# #     del dct['Jon']
# # print(dct)
#
# # set1 = {'rock', 'scissors', 'paper'}
# # set1 = {1,102,3, 400}
# # set2 = set()
# # set3 = set1.union(set2)
# # set3 = set1.intersection(set2)
# # set3 = set1 - set2
# # set3 = set1.difference(set2)
# # set3 = set2 - set1
# # for val in set1:
# #     if val > 100:
# #         set2.add(val)
# #
# # print(set1)
# # print(set2)
#
# # dct = {1: 'one', 2: 'two', 3: 'three'}
# # import pickle
# #
# # out_file = open('mydata.dat', 'wb')
# # pickle.dump(dct, out_file)
# # out_file.close()
# #
# # in_file = open('mydata.dat', 'rb')
# # dct2 = pickle.load(in_file)
# # in_file.close()
# # print(dct2)
#
# # moons_radiuses = {'Io': 1821.6, 'Europa': 1560.8, 'Ganymede': 2634.1, 'Callisto': 2410.3}
# # moons_gravity = {'Io': 1.796, 'Europa': 1.314, 'Ganymede': 1.428, 'Callisto': 1.235}
# # moons_orbital_period = {'Io': 1.769, 'Europa': 3.551,
# #                         'Ganymede': 7.154, 'Callisto': 16.689}
# #
# # moon_name = input('Enter moon name: ').strip()
# # print()
# # if moon_name in moons_gravity:
# #     print('Radius:', moons_radiuses[moon_name])
# #     print('Gravity:', moons_gravity[moon_name])
# #     print('Orbital period:', moons_orbital_period[moon_name])
# # else:
# #     print('Not correct moon name.')
#
#
# # def main():
# #     capitals = {'Ukraine': 'Kiev', 'Russia': 'Moscow', 'Italy': 'Rome'}
# #     good_answers = 0
# #     bad_answers = 0
# #     while len(capitals) > 0:
# #         country, capital = capitals.popitem()
# #         user_answer = input('Capital of ' + country + ' is ').strip()
# #         if user_answer == capital:
# #             print('Good!')
# #             good_answers += 1
# #         else:
# #             print('No. The capital name of', country, 'is', capital)
# #             bad_answers += 1
# #     print('Your score is', format(good_answers / (good_answers + bad_answers), '.0%'))
# #
# #
# # main()
#
#
# # def get_key(value, dct):
# #     for k, v in dct.items():
# #         if v == value:
# #             return k
# #     return None
# #
# #
# # def main():
# #     codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#'}
# #     file = open('encode.txt', 'r')
# #     result = ''
# #     for line in file:
# #         for ch in line:
# #             if ch in codes:
# #                 result += codes[ch]
# #             else:
# #                 result += ch
# #     file.close()
# #
# #     print(result)
# #
# #     file = open('decode.txt', 'w')
# #     file.write(result)
# #     file.close()
# #
# #     file = open('decode.txt', 'r')
# #     result = ''
# #     code_values = codes.values()
# #     for line in file:
# #         for ch in line:
# #             if ch in code_values:
# #                 result += get_key(ch, codes)
# #             else:
# #                 result += ch
# #     file.close()
# #     print(result)
# #
# #
# # main()
#
#
# # file = open('task_9.4.txt', 'r')
# # text = file.read()
# # file.close()
# #
# # words = text.split()
# # i = 0
# # while i < len(words):
# #     words[i] = words[i].strip('.,!?";[](){}|\\/*+#^~<>:')
# #     i += 1
# #
# # unique_words = set(words)
# # print(unique_words)
# # print(len(unique_words))
#
# # import random
# #
# # nums_frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
# #                     6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
# #
# # for i in range(100):
# #     rand_num = random.randint(1, 10)
# #     nums_frequencies[rand_num] += 1
# #
# # print(nums_frequencies)
# # import matplotlib.pyplot as plt
# # plt.pie(nums_frequencies.values(), labels=nums_frequencies.keys())
# # plt.show()
#
#
# # file = open('1.txt', 'r')
# # text1 = file.read()
# # file.close()
# #
# # words1 = text1.split()
# # i = 0
# # while i < len(words1):
# #     words1[i] = words1[i].strip('.,!?";[](){}|\\/*+#^~<>:')
# #     i += 1
# #
# # unique_words1 = set(words1)
# # # print(unique_words1)
# # # print(len(unique_words1))
# # # ========================
# # file = open('2.txt', 'r')
# # text2 = file.read()
# # file.close()
# #
# # words2 = text2.split()
# # i = 0
# # while i < len(words1):
# #     words2[i] = words2[i].strip('.,!?";[](){}|\\/*+#^~<>:')
# #     i += 1
# #
# # unique_words2 = set(words2)
# # # print(unique_words2)
# # # print(len(unique_words2))
# #
# # task1 = unique_words1 | unique_words2
# # print('Task 1')
# # print(task1)
# # print(len(task1))
# #
# # task2 = unique_words1 & unique_words2
# # print('Task 2')
# # print(task2)
# # print(len(task2))
# #
# # task3 = unique_words1 - unique_words2
# # print('Task 3')
# # print(task3)
# # print(len(task3))
# #
# # task4 = unique_words2 - unique_words1
# # print('Task 4')
# # print(task4)
# # print(len(task4))
# #
# # task5 = unique_words1 ^ unique_words2
# # print('Task 5')
# # print(task5)
# # print(len(task5))
#
#
# # file = open('WorldSeriesWinners.txt', 'r')
# # teams = []
# # for line in file:
# #     team = line.rstrip()
# #     teams.append(team)
# # file.close()
# # print(teams)
# # dct_winner_times = {}
# # for team in teams:
# #     if team not in dct_winner_times:
# #         dct_winner_times[team] = 1
# #     else:
# #         dct_winner_times[team] += 1
# #
# # print(dct_winner_times)
# #
# # year = 1903
# # dct_year_winner = {}
# # for team in teams:
# #     dct_year_winner[year] = team
# #     year += 1
# #     if year in (1904, 1994):
# #         year += 1
# #
# # print(dct_year_winner)
# #
# # year = int(input('Enter a year: ').rstrip())
# # if year in dct_year_winner:
# #     winner = dct_year_winner[year]
# #     print('In', year, 'wins', winner)
# #     print(winner, 'wins', dct_winner_times[winner], 'times.')
# # else:
# #     print('Sorry, in this year was no games.')
# # import pickle
# #
# #
# # def save_vegetables_prices(vegetables_prices, file):
# #     file_output = open(file, 'wb')
# #     pickle.dump(vegetables_prices, file_output)
# #     file_output.close()
# #
# #
# # def get_vegetables_prices(FILE_NAME):
# #     file = open(FILE_NAME, 'rb')
# #     vegetables_prices = pickle.load(file)
# #     file.close()
# #     return vegetables_prices
# #
# #
# # def show_menu():
# #     print()
# #     print('Vegetables & Prices')
# #     print('1. Show all vegetables & prices')
# #     print('2. Add a new vegetable & price')
# #     print('3. Change the price of an existing vegetable')
# #     print('4. Delete an existing vegetable & price')
# #     print('5. Exit')
# #     print()
# #
# #
# # def show_all_vegetables_prices(vegetables_prices):
# #     for name, price in vegetables_prices.items():
# #         print(str(name) + ': ' + format(vegetables_prices[name], '3.2f'))
# #
# #
# # def add_new_vegetable_price(vegetables_prices):
# #     name = input('Enter vegetable name: ').strip()
# #     price = float(input('Enter ' + name + ' price: '))
# #     vegetables_prices[name] = price
# #
# #
# # def change_price(vegetables_prices):
# #     name = input('Enter vegetable name: ').strip()
# #     if name not in vegetables_prices:
# #         print('There is no vegetable with name', name + '.')
# #         print('Try to add new vegetable.')
# #     else:
# #         price = float(input('Enter ' + name + ' price: '))
# #         vegetables_prices[name] = price
# #
# #
# # def delete_vegetable(vegetables_prices):
# #     name = input('Enter vegetable name: ').strip()
# #     if name not in vegetables_prices:
# #         print('There is no vegetable with name', name + '.')
# #     else:
# #         del vegetables_prices[name]
# #
# #
# # def main():
# #     FILE_NAME = 'vegetables_prices.dat'
# #     vegetables_prices = {}
# #     try:
# #         vegetables_prices = get_vegetables_prices(FILE_NAME)
# #         again = 'y'
# #         while again.lower() == 'y':
# #             show_menu()
# #             answer = int(input('Enter answer: '))
# #             if answer == 1:
# #                 show_all_vegetables_prices(vegetables_prices)
# #             elif answer == 2:
# #                 add_new_vegetable_price(vegetables_prices)
# #                 save_vegetables_prices(vegetables_prices, FILE_NAME)
# #             elif answer == 3:
# #                 change_price(vegetables_prices)
# #                 save_vegetables_prices(vegetables_prices, FILE_NAME)
# #             elif answer == 4:
# #                 delete_vegetable(vegetables_prices)
# #                 save_vegetables_prices(vegetables_prices, FILE_NAME)
# #             elif answer == 5:
# #                 exit(0)
# #             else:
# #                 print('Unknown answer.')
# #             again = input('Continue (y/n)? >>> ')
# #
# #     except IOError:
# #         # the file is not exists, because it's the first run,
# #         # then let's create the file
# #         again = 'y'
# #         while again.lower() == 'y':
# #             add_new_vegetable_price(vegetables_prices)
# #             again = input('Enter (y/n) to continue of exit: ').strip()
# #         save_vegetables_prices(vegetables_prices, FILE_NAME)
# #
# #
# # main()
#
#
# '''import random
#
#
# def create_deck():
#     deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
#             '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
#             '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
#             '10 of Spades': 10, 'Jack of Spades': 10,
#             'Queen of Spades': 10, 'King of Spades': 10,
#
#             'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
#             '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
#             '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
#             '10 of Hearts': 10, 'Jack of Hearts': 10,
#             'Queen of Hearts': 10, 'King of Hearts': 10,
#
#             'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
#             '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
#             '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
#             '10 of Clubs': 10, 'Jack of Clubs': 10,
#             'Queen of Clubs': 10, 'King of Clubs': 10,
#
#             'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
#             '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
#             '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
#             '10 of Diamonds': 10, 'Jack of Diamonds': 10,
#             'Queen of Diamonds': 10, 'King of Diamonds': 10
#             }
#     return deck
#
#
# def get_random_card_and_value(deck):
#     cards = tuple(deck.keys())
#     random_index = random.randrange(len(cards))
#     random_card = cards[random_index]
#     random_value = deck[random_card]
#     del deck[random_card]
#     return random_card, random_value
#
#
# def deal_cards(deck, number, hand_value=0):
#     if number > len(deck):
#         number = len(deck)
#
#     for count in range(number):
#         card, value = get_random_card_and_value(deck)
#         print(card)
#         # Ace -- it's only one type of card that can have value of 1 or 11
#         if card.startswith('Ace') and hand_value <= 10:
#             hand_value += 11
#         else:
#             hand_value += value
#
#     print('Value of this hand:', hand_value)
#     return hand_value
#
#
# def check_winner(hand_value1, hand_value2):
#     is_winner = False
#     if hand_value1 > 21:
#         print('Player 2 WINS!')
#         is_winner = True
#     if hand_value2 > 21:
#         print('Player 1 WINS')
#         is_winner = True
#     if hand_value1 == hand_value2 == 21:
#         print('Nobody wins')
#         is_winner = True
#     return is_winner
#
#
# def main():
#     deck = create_deck()
#     # num_cards = int(input('How many cards should I deal? '))
#     num_cards = 2
#
#     while len(deck) > 3:
#         is_winner = False
#         while not is_winner:
#             print('\tPlayer 1')
#             hand_value1 = deal_cards(deck, num_cards)
#             if hand_value1 < 21:
#                 hand_value1 += deal_cards(deck, 1, hand_value=hand_value1)
#             elif hand_value1 == 21:
#                 print('BLACKJACK!')
#
#             is_winner = check_winner(hand_value1, 0)
#
#             print('\tPlayer 2')
#             hand_value2 = deal_cards(deck, num_cards)
#             if hand_value2 < 21:
#                 hand_value2 += deal_cards(deck, 1, hand_value=hand_value2)
#             elif hand_value2 == 21:
#                 print('BLACKJACK!')
#
#             is_winner = check_winner(hand_value1, hand_value2)
#
#
# main()'''
#
# # import bank_account
# #
# #
# # def main():
# #     start_amount = float(input('Enter start amount to deposit: '))
# #     account = bank_account.BankAccount(start_amount)
# #     print(account)
# #     deposit_amount = float(input('How much do you want to deposit? >>> '))
# #     account.deposit(deposit_amount)
# #     print(account)
# #     withdraw_amount = float(input('How much do you want to withdraw? >>> '))
# #     account.withdraw(withdraw_amount)
# #     print(account)
# #
# #
# # main()
#
#
# import coin
#
# # def main():
#
#
# # mycoin = coin.Coin()
# # print('Start side up of the coin is', mycoin.get_sideup())
# # print('Tossing the coin 10 times...')
# # for i in range(10):
# #     mycoin.toss()
# #     print(mycoin.get_sideup())
# # print('Tossing the coin...')
# # mycoin.toss()
# # print('Current side up of the coin is', mycoin.get_sideup())
# #     coin1 = coin.Coin()
# #     coin2 = coin.Coin()
# #     coin3 = coin.Coin()
# #
# #     print('I have 3 coins with these sides up:')
# #     print(coin1.get_sideup())
# #     print(coin2.get_sideup())
# #     print(coin3.get_sideup())
# #     print()
# #
# #     print('I am tossing all 3 coins ...')
# #     print()
# #     coin1.toss()
# #     coin2.toss()
# #     coin3.toss()
# #
# #     print('Now here are the sides that are up:')
# #     print(coin1.get_sideup())
# #     print(coin2.get_sideup())
# #     print(coin3.get_sideup())
# #     print()
# #
# #
# # main()
#
# # class Book:
# #     def __init__(self, title, author, pages):
# #         self.__title = title
# #         self.__author = author
# #         self.__pages = pages
# #
# #     def __len__(self):
# #         return self.__pages
# #
# #     def __str__(self):
# #         return 'Title: ' + self.__title + \
# #                'Author: ' + self.__author + \
# #                'Pages: ' + self.__pages
# #
# #     def get_title(self):
# #         return self.__title
# #
# #     def get_author(self):
# #         return self.__author
# #
# #     def get_pages(self):
# #         return self.__pages
# #
# #     def set_title(self, title):
# #         self.__title = title
# #
# #     def set_author(self, author):
# #         self.__author = author
# #
# #     def set_pages(self, pages):
# #         self.__pages = pages
#
#
# # class Pet:
# #     def __init__(self, name, animal_type, age):
# #         self.__name = name
# #         self.__animal_type = animal_type
# #         self.__age = age
# #
# #     def set_name(self, name):
# #         self.__name = name
# #
# #     def set_animal_type(self, animal_type):
# #         self.__animal_type = animal_type
# #
# #     def set_age(self, age):
# #         self.__age = age
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_animal_type(self):
# #         return self.__animal_type
# #
# #     def get_age(self):
# #         return self.__age
# #
# #
# # def main():
# #     name = input('Enter name of a pet: ')
# #     animal_type = input('Enter type of a pet: ')
# #     age = input('Enter age of a pet: ')
# #     dog1 = Pet(name, animal_type, age)
# #     print()
# #     print('Name:', dog1.get_name())
# #     print('Animal type:', dog1.get_animal_type())
# #     print('Age:', dog1.get_age())
# #
# #
# # main()
#
#
# # class Car:
# #     def __init__(self, year_model, make):
# #         self.__year_model = year_model
# #         self.__make = make
# #         self.__speed = 0
# #
# #     def accelerate(self):
# #         self.__speed += 5
# #
# #     def brake(self):
# #         if self.__speed >= 5:
# #             self.__speed -= 5
# #         else:
# #             self.__speed = 0
# #
# #     def get_speed(self):
# #         return self.__speed
# #
# #
# # def main():
# #     car = Car(2021, 'Porsche')
# #     for count in range(5):
# #         car.accelerate()
# #         print(car.get_speed())
# #     for count in range(5):
# #         car.brake()
# #         print(car.get_speed())
# #
# #
# # main()
#
# # import pickle
# #
# #
# # class Employee:
# #     def __init__(self, name, id_number, department, job_title):
# #         self.__name = name
# #         self.__id_number = id_number
# #         self.__department = department
# #         self.__job_title = job_title
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_id_number(self):
# #         return self.__id_number
# #
# #     def get_department(self):
# #         return self.__department
# #
# #     def get_job_title(self):
# #         return self.__job_title
# #
# #     def set_name(self, name):
# #         self.__name = name
# #
# #     def set_id_number(self, id_number):
# #         self.__id_number = id_number
# #
# #     def set_department(self, department):
# #         self.__department = department
# #
# #     def set_job_title(self, job_title):
# #         self.__job_title = job_title
# #
# #     def __str__(self):
# #         return 'Name: ' + self.__name + \
# #                '\nID number: ' + str(self.__id_number) + \
# #                '\nDepartment: ' + self.__department + \
# #                '\nJob title: ' + self.__job_title
# #
# #
# # def main():
# #     # emp1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
# #     # emp2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
# #     # emp3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
# #     # print(emp1)
# #     # print()
# #     # print(emp2)
# #     # print()
# #     # print(emp3)
# #     # print()
# #
# #     # employees = {emp1.get_id_number(): emp1,
# #     #              emp2.get_id_number(): emp2,
# #     #              emp3.get_id_number(): emp3}
# #
# #     FILE_NAME = 'employees.dat'
# #     file = open(FILE_NAME, 'rb')
# #     employees = {}
# #     employees = pickle.load(file)
# #     file.close()
# #
# #     for k, v in employees.items():
# #         print(k)
# #         print(v)
# #         print()
# #
# #     # FILE_NAME = 'employees.dat'
# #     # file = open(FILE_NAME, 'wb')
# #     # pickle.dump(employees, file)
# #     # file.close()
# #
# #
# #
# # main()
#
# # class Bird:
# #     def __init__(self, bird_type):
# #         self.__bird_type = bird_type
# #
# #
# # class Duck(Bird):
# #     def __init__(self):
# #         Bird.__init__(self, 'duck')
#
#
# # class Employee:
# #     def __init__(self, name, number):
# #         self.__name = name
# #         self.__number = number
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_number(self):
# #         return self.__number
# #
# #     def set_name(self, name):
# #         self.__name = name
# #
# #     def set_number(self, number):
# #         self.__number = number
# #
# #
# # class ProductionWorker(Employee):
# #     def __init__(self, name, number, shift_number, hourly_pay_rate):
# #         Employee.__init__(self, name, number)
# #         self.__shift_number = shift_number
# #         self.__hourly_pay_rate = hourly_pay_rate
# #
# #     def get_shift_number(self):
# #         return self.__shift_number
# #
# #     def get_hourly_pay_rate(self):
# #         return self.__hourly_pay_rate
# #
# #     def set_shift_number(self, shift_number):
# #         self.__shift_number = shift_number
# #
# #     def set_hourly_pay_rate(self, hourly_pay_rate):
# #         self.__hourly_pay_rate = hourly_pay_rate
# #
# #
# # class ShiftSupervisor(Employee):
# #     def __init__(self, name, number, annual_salary, annual_production_bonus):
# #         Employee.__init__(self, name, number)
# #         self.__annual_salary = annual_salary
# #         self.__annual_production_bonus = annual_production_bonus
# #
# #     def get_annual_salary(self):
# #         return self.__annual_salary
# #
# #     def get_annual_production_bonus(self):
# #         return self.__annual_production_bonus
# #
# #     def set_annual_salary(self, annual_salary):
# #         self.__annual_salary = annual_salary
# #
# #     def set_annual_production_bonus(self, annual_production_bonus):
# #         self.__annual_production_bonus = annual_production_bonus
# #
# #
# # def main():
# #     print('\tShift supervisor info')
# #     name = input('Enter name: ')
# #     number = int(input('Enter number: '))
# #     annual_salary = float(input('Enter annual salary: '))
# #     annual_production_bonus = float(input('Enter annual production bonus: '))
# #     shift_supervisor = ShiftSupervisor(name, number, annual_salary, annual_production_bonus)
# #     print('Name:', shift_supervisor.get_name())
# #     print('Number:', shift_supervisor.get_number())
# #     print('Annual salary:', format(shift_supervisor.get_annual_salary(), ',.2f'))
# #     print('Annual production bonus:', format(shift_supervisor.get_annual_production_bonus(), ',.2f'))
# #
# #     # print('\tProduction worker info')
# #     # name = input('Enter name: ')
# #     # number = int(input('Enter number: '))
# #     # shift = int(input('Enter shift (1 or 2): '))
# #     # while shift not in (1, 2):
# #     #     shift = int(input('Enter valid shift (1 or 2): '))
# #     # hourly_pay_rate = float(input('Enter pay rate: '))
# #     # product_worker = ProductionWorker(name, number, shift, hourly_pay_rate)
# #     # print('Name:', product_worker.get_name())
# #     # print('Number:', product_worker.get_number())
# #     # print('Shift:', product_worker.get_shift_number())
# #     # print('Hourly pay rate:', product_worker.get_hourly_pay_rate())
# #
# #
# # main()
#
#
# # def massage(times):
# #     print('This is recursion function.')
# #     if times > 1:
# #         massage(times - 1)
# #
# #
# # def main():
# #     massage(5)
# #
# #
# # main()
#
#
# # def main():
# #     num = int(input('Enter a nonnegative number: '))
# #     fact = factorial(num)
# #     print('Factorial of', num, 'is', fact)
# #
# #
# # def factorial(num):
# #     if num == 0:
# #         return 1
# #     return num * factorial(num - 1)
# #
# #
# # main()
#
# # def range_sum(numbers, start, end):
# #     if start > end:
# #         return 0
# #     else:
# #         return numbers[start] + range_sum(numbers, start + 1, end)
# #
# #
# # def main():
# #     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# #     print(range_sum(numbers, 1, 4))
# #
# #
# # main()
#
#
# # def fibo(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibo(n - 1) + fibo(n - 2)
# #
# #
# # def main():
# #     for i in range(40):
# #         print(fibo(i))
# #
# #
# # main()
#
#
# # def gcd(x, y):
# #     if x % y == 0:
# #         return y
# #     else:
# #         return gcd(x, x % y)
# #
# #
# # print(gcd(49, 28))
#
#
# # def hanoi(num, from_, to_, temp_):
# #     if num > 0:
# #         hanoi(num - 1, from_, temp_, to_)
# #         print('Move disc from peg', from_, 'to peg', to_)
# #         hanoi(num - 1, temp_, to_, from_)
# #
# #
# # def main():
# #     hanoi(3, 1, 3, 2)
# #     print('All the discs are moved!')
# #
# #
# # main()
#
# # def show_me(word):
# #     print(word)
# #     if len(word) > 0:
# #         show_me(word[1:])
# #
# #
# # def main():
# #     show_me('word')
# #
# #
# # main()
#
#
# # def halver(num):
# #     print(num)
# #     half = num / 2
# #     if half >= 1:
# #         halver(half)
# #
# #
# # def main():
# #     halver(10)
# #
# #
# # main()
#
#
# # def queue(length):
# #     if length == 0:
# #         print('It is your turn.')
# #     else:
# #         print('Please wait.')
# #         queue(length - 1)
# # def queue(length):
# #     while length > 0:
# #         print('Please wait.')
# #         length = length - 1
# #     print('It is your turn.')
# #
# #
# # def main():
# #     queue(3)
# #
# #
# # main()
#
#
# # def print_desc(n):
# #     if n == 0:
# #         print(0)
# #     else:
# #         print(n)
# #         print_desc(n - 1)
# #
# #
# # def main():
# #     print_desc(5)
# #
# # main()
# #
# # def recursive_multiply(x, y):
# #     if x == 1:
# #         return y
# #     else:
# #         return y + recursive_multiply(x - 1, y)
# #
# #
# # def main():
# #     print(recursive_multiply(7, 4))
# #
# #
# # main()
#
# # def recursive_lines(n):
# #     if n > 0:
# #         recursive_lines(n - 1)
# #         print('*' * n)
# #
# #
# # def main():
# #     recursive_lines(3)
# #
# #
# # main()
#
#
# # def largest(lst):
# #     if len(lst) == 1:
# #         return lst[0]
# #     else:
# #         if lst[0] > lst[1]:
# #             lst[1] = lst[0]
# #         return largest(lst[1:])
# #
# #
# # def main():
# #     print(largest([1, 2, 3, 4, 5, 4, 3, 2, 1]))
# #
# #
# # main()
#
#
# # def rec_sum(lst):
# #     if len(lst) == 0:
# #         return 0
# #     else:
# #         return lst[0] + rec_sum(lst[1:])
# #
# #
# # def main():
# #     print(rec_sum([1, 2, 3, 4]))
# #
# #
# # main()
#
#
# # def is_palindrome(word):
# #     if len(word) < 2:
# #         return True
# #     elif word[0] == word[-1]:
# #         return is_palindrome(word[1:-1])
# #     else:
# #         return False
# #
# #
# # def main():
# #     words1 = ['', '1', '11', '111', '1111']
# #     words2 = ['12', '112', '1121', '11211', '121111', '211111']
# #     for word in words1:
# #         print(is_palindrome(word), end=' ')
# #     print()
# #     for word in words2:
# #         print(is_palindrome(word), end=' ')
#
#
# # main()
#
#
# # def rec_pow(x, y):
# #     if y == 0:
# #         return 1
# #     elif y == 1:
# #         return x
# #     else:
# #         return x * rec_pow(x, y - 1)
# #
# #
# # def main():
# #     print(rec_pow(2, 10))
# #
# #
# # main()
#
# # def ackermann(m, n):
# #     if m == 0:
# #         return n + 1
# #     if n == 0:
# #         return ackermann(m - 1, 1)
# #     else:
# #         return ackermann(m - 1, ackermann(m, n - 1))
# #
# #
# # def main():
# #     print(ackermann(3, 4))
# #
# #
# # main()
#
# # import tkinter
# #
# #
# # def main():
# #     main_window = tkinter.Tk()
# #     tkinter.mainloop()
# #
# #
# # main()
#
# # import tkinter
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.label1 = tkinter.Label(self.main_window,
# #                                     text='Hello World!')
# #         self.label2 = tkinter.Label(self.main_window,
# #                                     text='It\'s my GUI program.')
# #         self.label1.pack(side='top')
# #         self.label2.pack(side='top')
# #         tkinter.mainloop()
# #
# #
# # my_gui = MyGUI()
#
#
# # import tkinter
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.top_frame = tkinter.Frame(self.main_window)
# #         self.bottom_frame = tkinter.Frame(self.main_window)
# #         self.label1 = tkinter.Label(self.top_frame, text='Winker')
# #         self.label2 = tkinter.Label(self.top_frame, text='Blinker')
# #         self.label3 = tkinter.Label(self.top_frame, text='Nod')
# #         self.label1.pack(side='top')
# #         self.label2.pack(side='top')
# #         self.label3.pack(side='top')
# #
# #         self.label4 = tkinter.Label(self.bottom_frame, text='Winker')
# #         self.label5 = tkinter.Label(self.bottom_frame, text='Blinker')
# #         self.label6 = tkinter.Label(self.bottom_frame, text='Nod')
# #         self.label4.pack(side='left')
# #         self.label5.pack(side='left')
# #         self.label6.pack(side='left')
# #         self.top_frame.pack()
# #         self.bottom_frame.pack()
# #         tkinter.mainloop()
# #
# #
# # my_gui = MyGUI()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.button_show_messagebox = tkinter.Button(self.main_window,
# #                                                      text='Click me!',
# #                                                      command=self.do_something)
# #         self.button_quit = tkinter.Button(self.main_window,
# #                                           text='Exit',
# #                                           command=self.main_window.destroy)
# #         self.button_show_messagebox.pack()
# #         self.button_quit.pack()
# #         tkinter.mainloop()
# #
# #     def do_something(self):
# #         tkinter.messagebox.showinfo(title='You click the button',
# #                                     message='Thank you for clicking the button.')
# #
# #
# # my_gui = MyGUI()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class ConvertKmToMilesGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.value = tkinter.StringVar()
# #
# #         self.top_frame = tkinter.Frame(self.main_window)
# #         self.middle_frame = tkinter.Frame(self.main_window)
# #         self.bottom_frame = tkinter.Frame(self.main_window)
# #
# #         self.label_for_entry = tkinter.Label(self.top_frame,
# #                                              text='Enter kilometers:')
# #         self.entry_km = tkinter.Entry(self.top_frame,
# #                                       width=10)
# #         self.label_for_entry.pack(side='left')
# #         self.entry_km.pack(side='left')
# #
# #         self.label_descr_value = tkinter.Label(self.middle_frame,
# #                                                text='Converted to miles:')
# #         self.label_value = tkinter.Label(self.middle_frame,
# #                                          textvariable=self.value)
# #         self.label_descr_value.pack(side='left')
# #         self.label_value.pack(side='left')
# #
# #         self.button_calc = tkinter.Button(self.bottom_frame,
# #                                           text='Calculate',
# #                                           command=self.calculate)
# #         self.button_quit = tkinter.Button(self.bottom_frame,
# #                                           text='Exit',
# #                                           command=self.main_window.destroy)
# #         self.button_calc.pack(side='left')
# #         self.button_quit.pack(side='left')
# #         self.top_frame.pack()
# #         self.middle_frame.pack()
# #         self.bottom_frame.pack()
# #         tkinter.mainloop()
# #
# #     def calculate(self):
# #         km = float(self.entry_km.get())
# #         miles = km * 0.6214
# #         self.value.set(format(miles, ',.3f'))
# #         # tkinter.messagebox.showinfo(title='Result',
# #         #                             message='In ' + str(km) + ' km(s) is ' + str(miles) + ' miles.')
# #
# #
# # ConvertKmToMilesGUI()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class Show_Power:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.top_frame = tkinter.Frame(self.main_window)
# #         self.middle_frame1 = tkinter.Frame(self.main_window)
# #
# #         self.tip_label = tkinter.Label(self.top_frame,
# #                                        text='Choose an exponent')
# #         self.tip_label.pack()
# #
# #         self.radio_var = tkinter.IntVar()
# #         self.radio_var.set(3)
# #         self.pow2_radiobutton = tkinter.Radiobutton(self.middle_frame1,
# #                                                     text='2',
# #                                                     variable=self.radio_var,
# #                                                     value=2,
# #                                                     command=self.show_power)
# #         self.pow3_radiobutton = tkinter.Radiobutton(self.middle_frame1,
# #                                                     text='3',
# #                                                     variable=self.radio_var,
# #                                                     value=3,
# #                                                     command=self.show_power)
# #         self.pow2_radiobutton.pack(side='top')
# #         self.pow3_radiobutton.pack(side='top')
# #
# #         self.top_frame.pack()
# #         self.middle_frame1.pack()
# #         tkinter.mainloop()
# #
# #     def show_power(self):
# #         exp = self.radio_var.get()
# #         result = 2 ** exp
# #         tkinter.messagebox.showinfo(title='Result',
# #                                     message='2^' + str(exp) + ' = ' +
# #                                             str(result))
# #
# #
# # Show_Power()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class MyCheckbox:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.top_frame = tkinter.Frame(self.main_window)
# #         self.bottom_frame = tkinter.Frame(self.main_window)
# #         self.cb_var1 = tkinter.IntVar()
# #         self.checkbox_1 = tkinter.Checkbutton(self.top_frame,
# #                                               text='Option 1',
# #                                               variable=self.cb_var1)
# #         self.cb_var2 = tkinter.IntVar()
# #         self.checkbox_2 = tkinter.Checkbutton(self.top_frame,
# #                                               text='Option 2',
# #                                               variable=self.cb_var2)
# #         self.cb_var3 = tkinter.IntVar()
# #         self.checkbox_3 = tkinter.Checkbutton(self.top_frame,
# #                                               text='Option 3',
# #                                               variable=self.cb_var3)
# #         self.checkbox_1.pack(side='top')
# #         self.checkbox_2.pack(side='top')
# #         self.checkbox_3.pack(side='top')
# #
# #         self.button_info = tkinter.Button(self.bottom_frame,
# #                                           text='Info',
# #                                           command=self.show_info)
# #         self.button_quit = tkinter.Button(self.bottom_frame,
# #                                           text='Exit',
# #                                           command=self.main_window.destroy)
# #         self.button_info.pack(side='left')
# #         self.button_quit.pack(side='left')
# #
# #         self.top_frame.pack()
# #         self.bottom_frame.pack()
# #         tkinter.mainloop()
# #
# #     def show_info(self):
# #         msg = 'Checked checkbuttons:\n'
# #         if self.cb_var1.get() == 1:
# #             msg += '1\n'
# #         if self.cb_var2.get() == 1:
# #             msg += '2\n'
# #         if self.cb_var3.get() == 1:
# #             msg += '3\n'
# #         tkinter.messagebox.showinfo(title='Checkbuttons info',
# #                                     message=msg)
# #
# #
# # MyCheckbox()
#
# #
# # import tkinter
# # import random
# # import tkinter.font
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.canvas = tkinter.Canvas(self.main_window, width=600, height=1000)
# # coords = (10, 10, 189, 10, 100, 189, 10, 10)
# # self.canvas.create_line(coords)
# # self.canvas.create_rectangle(10, 10, 189, 189, fill='cyan', outline='blue')
#
# # self.canvas.create_rectangle(0, 0, 999, 999, fill='black')
# # for i in range(500):
# #     random_num = int(random.random() * 256 ** 3)
# #     random_color = '#' + hex(random_num)[2:].zfill(6)
# #     self.canvas.create_oval(2 + i, 2 + i, 999 - i, 999 - i, fill=random_color, outline=random_color)
#
# # self.canvas.create_arc(10, 10, 180, 180, start=0, extent=90, fill='cyan', style=tkinter.PIESLICE)
#
# # self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60, fill='cyan')
#
# #         i = 1
# #         for font_name in tkinter.font.families():
# #             self.font = tkinter.font.Font(family=font_name, size=12)
# #             self.canvas.create_text(10, 12 * i + 6, text=str(i) + font_name, anchor=tkinter.SW, font=self.font)
# #             i += 1
# #
# #         self.canvas.pack()
# #         tkinter.mainloop()
# #
# #
# # MyGUI()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         # tkinter.messagebox.showinfo(title='Info', message='Click OK when you are ready to continue')
# #         # self.frame = tkinter.Frame(self.main_window)
# #         # self.label1 = tkinter.Label(self.frame,
# #         #                             text='Programming is fun!')
# #         # self.label2 = tkinter.Label(self.frame,
# #         #                             text='Hello World!')
# #         # self.label1.pack(side='left')
# #         # self.label2.pack(side='left')
# #         # self.frame.pack()
# #         # self.entry_frame = tkinter.Frame(self.main_window)
# #         # # self.entry_var = tkinter.StringVar()
# #         # self.entry = tkinter.Entry(self.entry_frame)
# #         # self.entry.pack()
# #         #
# #         # self.button_frame = tkinter.Frame(self.main_window)
# #         # self.button = tkinter.Button(self.button_frame,
# #         #                              text='Calculate',
# #         #                              command=self.calculate)
# #         # self.button_quit = tkinter.Button(self.button_frame,
# #         #                                   text='Quit',
# #         #                                   command=self.main_window.destroy)
# #         # self.button.pack(side='left')
# #         # self.button_quit.pack(side='left')
# #         #
# #         # self.entry_frame.pack()
# #         # self.button_frame.pack()
# #         self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
# #         # self.canvas.create_line(0, 0, 199, 199, fill='blue', width=3)
# #         # self.canvas.create_rectangle(50, 50, 100, 100, outline='red', fill='black')
# #         # self.canvas.create_oval(50, 50, 150, 150, outline='lime')
# #         self.canvas.create_arc(20, 20, 180, 180, start=0, extent=90, fill='blue')
# #         self.canvas.pack()
# #         tkinter.mainloop()
# #
# #     # def calculate(self):
# #     # var = int(self.entry.get())
# #     # print(var)
# #     # print(type(var))
# #     # tkinter.messagebox.showinfo('Info', 'Button click.')
# #
# #
# # MyGUI()
#
#
# # import tkinter
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.label_frame = tkinter.Frame(self.main_window)
# #         self.text_info = tkinter.StringVar()
# #         self.label_info = tkinter.Label(self.label_frame,
# #                                         textvariable=self.text_info)
# #         self.label_info.pack()
# #         self.button_frame = tkinter.Frame(self.main_window)
# #         self.show_info_button = tkinter.Button(self.button_frame,
# #                                                text='Show Info',
# #                                                command=self.show_info)
# #         self.quit_button = tkinter.Button(self.button_frame,
# #                                           text='Quit',
# #                                           command=self.main_window.destroy)
# #         self.show_info_button.pack(side='left')
# #         self.quit_button.pack(side='left')
# #
# #         self.label_frame.pack()
# #         self.button_frame.pack()
# #         tkinter.mainloop()
# #
# #     def show_info(self):
# #         self.text_info.set('Vatskaya Street\n' +
# #                            '59\n' +
# #                            'Kharkov, Ukraine, 61068')
# #
# #
# # MyGUI()
#
#
# # import tkinter as tk
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.PRICES = {'coffee': 9.99, 'cream': 0.99}
# #
# #         self.main_window = tk.Tk()
# #         self.checkbuttons_frame = tk.Frame(self.main_window)
# #         self.labels_frame = tk.Frame(self.main_window)
# #         self.buttons_frame = tk.Frame(self.main_window)
# #         self.create_checkbutton_coffee()
# #         self.create_checkbutton_cream()
# #
# #         self.show_total_button = tk.Button(self.buttons_frame,
# #                                            text='Show Total Price',
# #                                            command=self.show_total_price)
# #         self.show_total_button.pack(side='left')
# #
# #         self.total_price_tip_label = tk.Label(self.labels_frame,
# #                                               text='Total Price: ')
# #         self.total_price_stringvar = tk.StringVar()
# #         self.total_price_value_label = tk.Label(self.labels_frame,
# #                                                 textvariable=self.total_price_stringvar)
# #         self.total_price_tip_label.pack(side='left')
# #         self.total_price_value_label.pack(side='left')
# #
# #         self.checkbuttons_frame.pack()
# #         self.labels_frame.pack()
# #         self.buttons_frame.pack()
# #         tk.mainloop()
# #
# #     def show_total_price(self):
# #         total = 0.0
# #         if self.coffee_intvar.get() == 1:
# #             total += self.PRICES['coffee']
# #         if self.cream_intvar.get() == 1:
# #             total += self.PRICES['cream']
# #         self.total_price_stringvar.set(format(total, '.2f'))
# #
# #     def create_checkbutton_coffee(self):
# #         self.coffee_intvar = tk.IntVar()
# #         self.coffee_intvar.set(1)
# #         self.cb_coffee = tk.Checkbutton(self.checkbuttons_frame,
# #                                         text='Coffee - ' + str(self.PRICES['coffee']),
# #                                         variable=self.coffee_intvar)
# #         self.cb_coffee.pack()
# #
# #     def create_checkbutton_cream(self):
# #         self.cream_intvar = tk.IntVar()
# #         self.cream_intvar.set(1)
# #         self.cb_cream = tk.Checkbutton(self.checkbuttons_frame,
# #                                        text='Cream - ' + str(self.PRICES['cream']),
# #                                        variable=self.cream_intvar)
# #         self.cb_cream.pack()
# #
# #
# # MyGUI()
#
#
# # import tkinter
# # import tkinter.messagebox
# #
# #
# # class MyGUI:
# #     def __init__(self):
# #         self.main_window = tkinter.Tk()
# #         self.num1_entry = tkinter.Entry(self.main_window)
# #         self.operation_entry = tkinter.Entry(self.main_window)
# #         self.num2_entry = tkinter.Entry(self.main_window)
# #         self.calc_button = tkinter.Button(self.main_window,
# #                                           text=' = ',
# #                                           command=self.calculate)
# #         self.result = tkinter.StringVar()
# #         self.result_entry = tkinter.Entry(self.main_window,
# #                                           textvariable=self.result)
# #
# #         self.num1_entry.pack(side='left')
# #         self.operation_entry.pack(side='left')
# #         self.num2_entry.pack(side='left')
# #         self.calc_button.pack(side='left')
# #         self.result_entry.pack(side='left')
# #         tkinter.mainloop()
# #
# #     def calculate(self):
# #         operation = self.operation_entry.get().strip()
# #         result = 0
# #         if operation in ('+', '-', '*', '**', '/'):
# #             num1 = float(self.num1_entry.get())
# #             num2 = float(self.num2_entry.get())
# #             if operation == '+':
# #                 result = num1 + num2
# #             elif operation == '-':
# #                 result = num1 - num2
# #             self.result.set(result)
# #         else:
# #             tkinter.messagebox.showerror(title='Error',
# #                                          message='Wrong operation."' + operation + '"')
# #
# #
# # MyGUI()
#
# # x = [1, 2, 3]
# # print(id(x))
# # print(id([1, 2, 3]))
#
# # x = [1, 2, 3]
# # y = x
# # print(y is x)
# # print(y is [1, 2, 3])
#
# # x = [1, 2, 3]
# # y = x
# # print(y is x)
# # x.append(4)
# # print(x)
# # print(y)
#
# # x = [1, 2, 3]
# # y = x
# # y.append(4)
# #
# # s = "123"
# # t = s
# # t = t + "4"
# #
# # print(str(x) + " " + s)
#
# # x = [1, 2, 3]
# # print(type(x))
# # print(type(4))
# # print(type(type(4)))
#
# # objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
# # my_set = set()
# # for obj in objects:
# #     my_set.add(id(obj))
# # ans = len(my_set)
# # print(ans)
# # print(my_set)
# # print(len(objects))
#
# # ans = 0
# # for y in range(len(objects)):
# #     for x in range(y+1, len(objects)):
# #         if y == x: continue
# #         if objects[y] is objects[x]:
# #             ans += 1
# #
# # print(ans)
#
# # my_set = set(objects)
# # ans = len(objects) - len(my_set)
# # # print(ans)
# #
# # # ans = 0
# # unique_elements = []
# # for obj in objects:
# #     if obj not in my_set:
# #         unique_elements.append(obj)
# #         ans += 1
# #
# # print(len(unique_elements))
#
#
# # def function_name(arg1, arg2):
# #     return arg1 + arg2
# #
# #
# # print(type(function_name))
# # print(id(function_name))
#
# # def list_sum(lst):
# #     result = 0
# #     for element in lst:
# #         result += element
# #     return result
# #
# #
# # def sum(a, b):
# #     return a + b
# #
# #
# # y = sum(14, 29)
# # z = list_sum([1, 2, 3])
# # print(y)
# # print(z)
#
# # a = []
# #
# # def foo(arg1, arg2):
# #   a.append("foo")
# #
# # foo(a.append("arg1"), a.append("arg2"))
# #
# # print(a)
# #
# # a = []
# # a.append(1)
# # a.append(2)
# # a.append(3)
# # print(a)
# # a.pop()
# # print(a)
# # a.pop()
# # print(a)
#
# # def run_func(func):
# #     func()
# #
# #
# # def say_hi():
# #     print('Hi!')
# #
# #
# # run_func(say_hi)
#
# # def closest_mod_5(x):
# #     if x % 5 == 0:
# #         return x
# #     return closest_mod_5(x + 1)
# #
# # print(closest_mod_5(26))
#
# # lst = [1, 2, 3, 4, 5]
# # res = map(lambda x: x*x, lst)
# # print(res)
# # print(type(res))
# # print(list(res))
#
# # n, k = map(int, input().split())
# #
# #
# # def C(n, k):
# #     if k == 0:
# #         return 1
# #     elif k > n:
# #         return 0
# #     else:
# #         return C(n - 1, k) + C(n - 1, k - 1)
# #
# #
# # print(C(n, k))
#
# # class Counter:
# #     def __init__(self):
# #         self.count = 0
# #
# #     def inc(self):
# #         self.count += 1
# #
# #     def dec(self):
# #         self.count -= 1
# #
# #     def reset(self):
# #         self.count = 0
# #
# #     def __str__(self):
# #         return str(self.count)
# #
# #
# # x = Counter()
# # print(x)
# # x.inc()
# # x.inc()
# # print(x)
# # Counter.inc(x)
# # print(x)
#
# # class MoneyBox:
# #     def __init__(self, capacity):
# #         self.capacity = capacity
# #         self.added = 0
# #
# #     def can_add(self, v):
# #         return (self.capacity - self.added) >= v
# #
# #     def add(self, v):
# #         if self.can_add(v):
# #             self.added += v
# #
# #
# # mb = MoneyBox(100)
# # print(mb.can_add(98))
# # mb.add(98)
# # mb.add(1)
# # mb.add(1)
# # mb.add(1)
# # print(mb.added)
#
#
# # class Buffer:
# #     def __init__(self):
# #         self.seq = []
# #         self.buf = []
# #         self.summm = 0
# #
# #     def add(self, *a):
# #         self.seq.append(a)
# #         last_max_5_elements = 5 - len(a) % 5
# #         self.buf.append(a[-last_max_5_elements:])
# #         self.summm = self.summ(self.buf)
# #         print(self.summm)
# #
# #     def get_current_part(self):
# #         print(self.seq)
# #         return self.buf
# #
# #     def summ(self, args):
# #         total = 0
# #         for arg in args:
# #             total = total + arg
# #         return total
# #
# #
# # buf = Buffer()
# # buf.add(1, 2, 3)
# # buf.get_current_part()  # вернуть [1, 2, 3]
# # buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# # buf.get_current_part()  # вернуть [6]
# # buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# # buf.get_current_part()  # вернуть []
# # buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# # buf.get_current_part()  # вернуть [1]
#
# # from math import pi
# #
# # areas = {'square': lambda a: a * a,
# #          'rectangle': lambda a, b: a * b,
# #          'circle': lambda r: pi * r * r,
# #          'sphere': lambda r: 4 * pi * r * r}
# #
# # print(areas['circle'](10))
#
# # print((lambda x, y: x + y)(2, 3))
# # func1 = lambda x, y: x + y
# # seq1 = (1, 2, 3, 4, 5)
# # seq2 = (9, 8, 7, 6, 5)
# # print(list(map(func1, seq1, seq2)))
#
# # is_odd = lambda x: x % 2 == 1
# # seq = range(1, 21)
# # odds = filter(is_odd, seq)
# # print(list(odds))
#
# # is_vovel = lambda x: x in ('a', 'e', 'i', 'o', 'u', 'y')
# # text = 'Almost all time I fell nothing.'
# # letters = filter(is_vovel, text)
# # # print(letters)
# # for letter in letters:
# #     print(letter, end='')
# # from functools import reduce
# #
# # nums = (1, 2, 3, 4, 5)
# # sum = reduce(lambda x, y: x + y, nums)
# # print(sum)
#
# # x = 'abc'
# # y = 'xyz'
# # print(tuple(zip(x, y)))
# # x2, y2 = zip(*zip(x, y))
# # print(''.join(x2))
# # print(y2)
#
# # code = lambda tup: tup[1].upper() + str(tup[0])
# # print(list(map(code, enumerate('abc'))))
#
# # print({x: x * x for x in [1, 2, 3, 4, 5] if x % 2 == 1})
# # a = [1, 2, 3, 4]
# # b = [9, 8, 7, 6]
# # s = [x + y for x, y in zip(a, b)]
# # print(s)
#
# # show = lambda: print(5)
# # show()
#
# # def adder(n):
# #     def fn(m):
# #         return n + m
# #
# #     return fn
# #
# #
# # print(adder(2)(3))
#
# # def make_adder():
# #     n = 0
# #
# #     def fn(x):
# #         nonlocal n
# #         n += x
# #         return n
# #
# #     return fn
# #
# #
# # my_adder = make_adder()
# # print(my_adder(3))
# # print(my_adder(3))
# # print(my_adder(3))
#
#
# # def pipe(data, *fns):
# #     for fn in fns:
# #         data = fn(data)
# #     return data
# #
# #
# # print(pipe(2,
# #            lambda x: x + 5,
# #            lambda x: x * x))
#
# # def my_sum(a, b, c):
# #     return a + b + c
# #
# #
# # lst = [1, 2, 3]
# # print(my_sum(*lst))
#
# # a = 1.2
# # b = 555
# # c = 'Nick'
# # print(f'A = {a}, B = {b}, C = {c}. A + B = {a+b}')
#
# # print(int('0xFF', base=16))
# print(dir())
# print(globals())
#
#
# def fn():
#     var = 5
#     print(locals())
#
# fn()

# x = [1, 2, 3, 4, 5]
# x[1:4] = [55, 99]
# print(x)

# import os

# print(os.getlogin())

# print(os.getcwd())
# os.chdir('C:\\')
# print(os.getcwd())
# filename = os.path.join('c:\\', 'ФОТО')
# print(filename)
# lst = os.listdir('.')
# dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# for dir in dirs:
#     print(dir)
# print()
# for file in files:
#     print(file)

# import os
#
#
# def show_files(path, tabs_count=0):
#     os.chdir(path)
#     files = os.listdir()
#     for file in files:
#         if os.path.isdir(file):
#             print(file)
#             tabs_count += 1
#             show_files(file, tabs_count)
#             tabs_count -= 1
#         else:
#             print('  ' * (tabs_count-1) + file)
#
#
# os.chdir(os.path.join('c:\\', '[Udemy] Станьте Мастером Математического Анализа. Calculus 1-3'))
# show_files(os.getcwd())

# print(divmod(5, 2))

# a = (3+5j)/(1-2j)
# print(a)

# b = (7+3j)/4j
# print(b)
# print( (1j * 1j).imag)

# from cmath import *
# from math import *
# print(sqrt(25))

# print(int(float(input())))

# import xmltodict
#
# XML_FILE_NAME = 'XML/BINAD.CCUR_FUT.GALAUSDT_Settings_4KHhv_original.xml'
#
# with open(XML_FILE_NAME, 'r', encoding='utf-8') as f:
#     xml = xmltodict.parse(f.read(), encoding='utf-8')
#
# print(xml)
# xml['Settings']['DOM']['AutoScroll']['@Value'] = str(False)
# print(xml)
#
# with open(XML_FILE_NAME, 'w', encoding='utf-8') as f:
#     f.write(xmltodict.unparse(xml, pretty=True, short_empty_elements=True, full_document=True, encoding='utf-8'))
#
#
# def change_tabs_to_spaces(xml_lines):
#     for i in range(len(xml_lines)):
#         old_len = len(xml_lines[i])
#         xml_lines[i] = xml_lines[i].lstrip()
#         new_len = len(xml_lines[i])
#         diff = old_len - new_len # coun
#         xml_lines[i] = ' ' * diff * 2 + xml_lines[i]
#
#
# def add_space_in_front_of_backslash(xml_lines):
#     for i in range(len(xml_lines)):
#         xml_lines[i] = xml_lines[i].replace('/>', ' />')
#
#
# f = open(XML_FILE_NAME, 'r', encoding='utf-8')
# xml_lines = f.readlines()
# f.close()
#
# change_tabs_to_spaces(xml_lines)
# add_space_in_front_of_backslash(xml_lines)
#
# with open(XML_FILE_NAME, 'w', encoding='utf-8') as f:
#     f.writelines(xml_lines)


# lst = [1, 2, 3, 4, 5]
# # print(lst[(len(lst) + 1) // 2:])
# # lst[len(lst):] = [6, 7]
# # lst[:0] = [-2, -1, 0]
# lst[2:-1] = []
# print(lst)
# lst.extend([6, 7, 8])
# print(lst)
# # lst.insert(0, 'start')
# # lst.insert(3, 4)
# # lst.insert(len(lst), 'end')
# lst[0:0] = [0]
# print(lst)
# del lst[:3]
# print(lst)


# lst = list(range(1, 11))
# print(lst)
# # lst[0:0] = lst[-3:]
# # lst.insert(0, lst[-3:])
# lst = lst[-3:] + lst[:-3]
# print(lst)

# lst = [4, 1, 5, 2, 3]
# print(sorted(lst, reverse=True))

# x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
# print(sorted(x))

# def compare_str_len(string):
#     return len(string)
#
#
# import random
#
#
# def shuffle_strings(string):
#     return random.randint(1, int(1e20))
#
#
# lst = ['alone', 'banana', 'cat']
# print(sorted(lst, key=compare_str_len, reverse=True))
# print(sorted(lst, key=shuffle_strings, reverse=True))


# lst = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
#
#
# def sort_from_2nd_element(lst):
#     return lst[1]
#
#
# print(sorted(lst, key=sort_from_2nd_element))

# qubits = 2 ** 1121
# print(qubits)
# print(len(str(2 ** 1121)))

# lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
# for i in range(1, 6):
#     print(i, '-', lst.count(i))

# lst = [1, 1, 1, 1, 1]
# print(sum(lst))


# print([[1,2]] * 3)

# lst = [1, 2, 3, 4]
# print(lst)
# if 1 in lst and lst.count(1) > 1:
#     lst.remove(1)
# print(lst)

# import copy
#
# lst = [[0], 1]
# shallow = lst[:]
# deep = copy.deepcopy(lst)
# print(lst[0])
# # shallow[0][0] = 'zero'
# deep[0][0] = 'zero'
# print(lst[0])
# print(deep[0])

# x = [1,2,3]
# tup = (x, 0, 1)
# print(tup)
# del tup[0][0]
# print(tup)

# print(type((1,2)))

# one, two, three = (1, 2, 3)
# print(one)
# x = (3, 1, 4, 2)
# print(x)
# x = tuple(sorted(x))
# print(x)

# print(list('abcdef'))
# a, b, *c = 1, 2, 3, 4, 5
# print(*c)

# print(frozenset([1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)]))

# temperatures = []
# with open('lab_05.txt', 'r') as f:
#     for row in f:
#         temperatures.append(float(row.strip()))

# print(temperatures)
# print('\tTemperatures')
# print('Highest:', max(temperatures))
# print('Lowest:', min(temperatures))
# print('Average:', format(sum(temperatures) / len(temperatures), '.1f'))
# temperatures.sort()
# if len(temperatures) % 2 == 1:
#     median = temperatures[len(temperatures) // 2 + 1]
# else:
#     median = (temperatures[len(temperatures) // 2] +
#               temperatures[len(temperatures) // 2 + 1]) / 2
#
# print('Median:', median)
# print(len(temperatures))
# print(len(set(temperatures)))

# print('\155\x6Dm')
# print('\n\012\x0A')
# print('\155\x6Dm')

# print('\N{LATIN SMALL LETTER A WITH ACUTE}')
# print("\u00E1")

# import os

# for p in os.listdir('.'):
#     print(p)

# print(os.getcwd())
# print(os.listdir(os.curdir))
# os.chdir('C:/')
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

# import pathlib
# cur_path = pathlib.Path()
# print(cur_path.cwd())

# import os
# print(os.path.join('bin', 'users/files/utilities', 'python'))

# import os
# print(os.path.split(os.path.join('some', 'directory', 'path')))
# print(os.path.basename(os.path.join('some', 'directory', 'path')))
# print(os.path.dirname(os.path.join('some', 'directory', 'path')))
# print(os.path.splitext(os.path.join('some', 'directory', 'path.jpg')))

# import os
# from pathlib import Path
# path = Path('some', 'directory', 'path.jpg')
# print(path.name)
# print(path.parent)
# print(path.suffix)

# import os
# print(os.name)

# import sys
# print(sys.platform)

# import os

# print(os.path.isfile(r'C:\Users\NickSky\AppData\Local\Programs\Python\Python310\python.exe'))
# print(os.path.isdir(r'C:\Users\NickSky\AppData\Local\Programs\Python\Python310\python.exe'))
# print(os.path.exists(r'C:\Users\NickSky\AppData\Local\Programs\Python\Python310\python.exe'))
# print(os.path.samefile(r'D:\Money\Скальпинг\Python\MySoft\Gaddis\text.txt',
#                        r'D:\Money\Скальпинг\Python\MySoft\Gaddis\text2.txt'))
# print(os.path.getctime(r'D:\Money\Скальпинг\Python\MySoft\Gaddis\text.txt'))

# import os

# with os.scandir('.') as my_dir:
#     for entry in my_dir:
#         print(entry.name, entry.is_file())

# print(os.path.split(r'D:\Money\Скальпинг\Python\MySoft\Gaddis\text.txt'))
# for root, dirs, files in os.walk(os.curdir):
#     print('{0} has {1} files'.format(root, len(files)))


# print(os.path.getsize(r'C:\Users\NickSky\AppData\Local\Programs\Python\Python310\python.exe'))
# import glob

# print(glob.glob('[0-9].py'))
# import os
# import glob
# import shutil
#
# path_to_tmp_files = r'C:\Program Files (x86)\FSR Launcher\SubApps\CScalp\Data\MVS'
# os.chdir(path_to_tmp_files)
#
# files = glob.glob('BINAD.CCUR*.tmp')
# unique_dir_name = str(id('unique_id_to_create_unique_dir_name'))
# full_path_to_new_dir = os.path.join(path_to_tmp_files, unique_dir_name)
#
# os.mkdir(full_path_to_new_dir)
#
# for file in files:
#     full_path_to_tmp_file = os.path.join(path_to_tmp_files, file)
#     full_path_to_copy_of_tmp_file = os.path.join(full_path_to_new_dir, file)
#     shutil.copyfile(full_path_to_tmp_file, full_path_to_copy_of_tmp_file)
#
# base_name = os.path.join(path_to_tmp_files, 'xml_settings_backup')
# shutil.make_archive(base_name=base_name, format='zip', root_dir=full_path_to_new_dir)
# shutil.rmtree(path=full_path_to_new_dir)


# file = open('4.py', encoding='utf-8')
# count = len(file.readlines())
# print(count)
# file.close()
#
# import sys
# # sys.stdout.write('Some string')
# s = sys.stdin.readline()
# print(s)
# 123


# import sys
# f = open('outputfile.txt', 'w')
# sys.stdout = f
# sys.stdout.writelines(['one', 'two'])
# print('Some string')
# f.close()
# sys.stdout = sys.__stdout__
# print('Some string 2')

# f = open('outputfile.txt', 'w')
# print('qqq', file=f)
# f.close()

# some_dict = {(1, 2, 3): 'one_two_three'}
# print(some_dict[(1, 2, 3)])

# import struct
# record_format = '>hd4s'
# record_size = struct.calcsize(record_format)
# print(record_size)
# with open('data.dat', 'wb') as f:
#     f.write(struct.pack(record_format, 7, 3.14, b'good'))

# import pickle
# f = open('data2.dat', 'wb')
# pickle.dump(7, f)
# pickle.dump(3.14, f)
# pickle.dump(b'good', f)
# f.close()
# f = open('data2.dat', 'rb')
# a = pickle.load(f)
# b = pickle.load(f)
# c = pickle.load(f)
# print(a, b, c, sep='\n')
# f.close()

# import struct
#
# record_format = '>hd4s'
# record_size = struct.calcsize(record_format)
# result_list = []
# f = open('data.dat', 'rb')
# while 1:
#     try:
#         record = f.read(record_size)
#         if record == '':
#             f.close()
#             break
#         result_list.append(struct.unpack(record_format, record))
#     except Exception:
#         pass
#     print(result_list)
#     break

import shelve
# book = shelve.open('addresses')
# # book['shcheglov'] = ('nick', '0661889110', 'Viatska Street, 59')
# book['ivanov'] = ('petr', '0661234567', 'Sumska Street, 1')
# book.close()

# book = shelve.open('addresses')
# for key in book.keys():
#     print(book[key])
# book.close()

