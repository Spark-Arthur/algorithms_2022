"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""

from random import randint
from pympler.asizeof import asizeof
from numpy import array

'''
Курс основ python урок 6 задание 2:
Дан список, заполненный произвольными числами.
Получить список из элементов исходного, удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.
'''


def original():
    numbers = [randint(-200, 200) for num in range(100)]
    res = [num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0]
    del numbers
    return res


def optimized():
    numbers = array([randint(-200, 200) for num in range(100)])
    res = array([num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0])
    del numbers
    return res



print('original', asizeof(original()))
del original
print('optimized', asizeof(optimized()))
del optimized

"""
Вывод: Использовал Array, получилось хорошо оптимизировать память
"""