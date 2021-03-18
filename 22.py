'''
Условие задачи:
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4

Sample Input 2:
10
Sample Output 2:

Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3

Sample Input 4:
1 1 1 1 1 2 2 2
Sample Output 4:
1 2
'''

#Code
a = [int(i) for i in input().split()]
a.sort()
n = 0
for h in a:
    i = a.count(a[n])
    if i > 1:
        print(a[n], ' ', end="")
        while i > 2:
            del a[n]
            i -= 1

        del a[n]
        n += 1
    elif i == 1:
        n += 1



