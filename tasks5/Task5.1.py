import sys
import os


with open('task1.txt', 'w') as task1:
    print('Введите необходимые строки. Для завершения записи введите последнюю строку пустой: ')
    for line in sys.stdin:
        if not line or line == '\n':
            sys.exit(f"Файл был успешно записан. Вы можете найти его по адресу {os.path.join(os.getcwd(), 'task1.txt')}")
        else:
            task1.write(line)
