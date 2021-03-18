'''
Условие задачи:
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

Sample Input 1:
5
-3
8
4
0
Sample Output 1:
14
Sample Input 2:
0
Sample Output 2:
0
'''

#Code
# put your python code here
n = int(input())
s = n
while n != 0:
    n = int(input())
    i = n
    s += i
print(s)



