import sys
import os


with open('task5.txt', 'w+') as task5:
    print('Введите набор чисел, разделённых пробелами: ')
    for line in sys.stdin:
        if any([line == '\n', not line]):
            break
        task5.write(line)
with open('task5.txt', 'r') as task5:
    sum_line = task5.readline()
    total = sum(map(float, sum_line.split()))
print('Cумма введённых чисел равна {}'.format(total))
print(f"Файл был успешно записан. Вы можете найти его по адресу {os.path.join(os.getcwd(), 'task5.txt')}")

#не могу понть в чм ошибка
