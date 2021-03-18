'''
Условие задачи:
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:
8
2
14
Sample Output 1:
14
2
8

Sample Input 2:
23
23
21
Sample Output 2:
23
21
23
'''

#Code
# put your python code here
a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print(a, '\n', c, '\n', b)
elif a >= c >= b:
    print(a, '\n', b, '\n', c)
elif b >= c >= a:
    print(b, '\n', a, '\n', c)
elif b >= a >= c:
    print(b, '\n', c, '\n', a)
elif c >= a >= b:
    print(c, '\n', b, '\n', a)
elif c >= b >= a:
    print(c, '\n', a, '\n', b)





