"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    nl = list(str(enter_num))
    nl.reverse()
    num = "".join(nl)
    return num


num = 7753192

print(f'1 - {timeit("revers_1(num)", globals=globals(), number=10000)}')
print(f'2 - {timeit("revers_2(num)", globals=globals(), number=10000)}')
print(f'3 - {timeit("revers_3(num)", globals=globals(), number=10000)}')
print(f'4 - {timeit("revers_4(num)", globals=globals(), number=10000)}')


"""
Вывод: эффективнее всего revers_3 т.к он использует срез, соответственно обращается на прямую.
"""