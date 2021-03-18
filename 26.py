'''
Условие задачи:
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.
'''

#Code
def modify_list(l):
    k = 0
    i = -1

    while k <= len(l):
        if len(l) == 1:
            if l[0] % 2 != 0:
                del l[0]
                break
            else:
                l[0] = l[0] // 2
                break
        elif l[i] % 2 != 0:
            del l[i]
            k = 0
        elif l[i] % 2 == 0:
            l[i] = l[i] // 2
            i -= 1
        if len(l) + i < 0:
            break
        k += 1

