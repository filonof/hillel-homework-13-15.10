# 1

'''
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
'''

def change(lst: list) -> list:

    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

A = [6, 1, 'qwerty', 19 - 3, 'admin', 'wasd']

print(change(A))
print()

# 2

'''
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
'''

def to_dict(lst):

    A = dict(zip(lst, lst))
    return A

lst = ['admin', 123, 'password', 9, 'qwerty', 6,]

print(to_dict(lst))
print()

# 3

'''
Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
'''

def sum_range(start: int, end: int):

    num = 0
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        num += i
    return num

print(sum_range(2, 5))
print()

# 4

'''
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
'''


def read_last(lines, file):

    if lines > 0:
        A = open(file, 'r')
        string = A.readlines()[-lines:]
        for i in string:
            print(i)
        A.close()
    else:
        print("Error! Number must be positive.")

read_last(3, 'file_folder.txt')
