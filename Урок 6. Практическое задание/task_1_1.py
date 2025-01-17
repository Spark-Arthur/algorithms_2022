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

Это файл для первого скрипта
"""
from pympler.asizeof import asizeof

"""
Видеокурс основ python урок 4 задание 3:
Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
В этом случае ответ будет:
[5, 8]
"""
my_list_1 = [1, 6, 5, 56, 8, 2, 12, 2, 7, 5, 12, 8, 2, 12, 2, 32, 5, 12, 8, 123, 12, 2, 7, 5, 12, 8, 2, 0]


def original():
    res = []
    for num in my_list_1:
        if my_list_1.count(num) == 1:
            res.append(num)
    return res


def optimized():
    for i in my_list_1:
        if i % 2 == 0:
            yield i


print('original', asizeof(original()))
print('optimized', asizeof(optimized()))

"""
Вывод: Создал генератор, занимает меньше памяти, но при часто повторяющихся элементах в списке меньше занимает original
"""
