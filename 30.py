'''
Условие задачи:
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

#Code
with open('dataset_3363_3.txt') as i:
    a=i.read().strip().split()
a.sort()
c = []
i = 0
k = 1

for x in a:
    if k >= len(a):
        break
    if a[i] != a[k]:
        i += 1
        k += 1
        continue

    while a[i] == a[k]:
        k += 1
        if k >= len(a):
            break
    c.append(a[i])
    b = a.count(a[i])
    c.append(b)
    i = k
    k += 1

r = []
n = 1
m = 0

while m < len(c):
    r.append(c[n])
    n += 2
    m += 2
e = max(r)
m = 0
y = []
for x in c:
    if c[m] == e:
        m -= 1
        y.append(c[m])
        y.append(e)
        m += 1
    m += 1
n = 0
m = 2

if len(y) > 2:
    for x in y:
        if n > len(y):
            break
        if y[m] < y[n]:
            n += 2
        else:
            m = n
else:
    res=(print(y[0], y[1]))


with open('answer_3363_3.txt','w') as g:
    g.write('T 12\n')

