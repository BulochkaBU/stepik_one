'''
Условие задачи:
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''

#Code
n = int(input())
k = []
for x in range(n):
    a = input().split(';')
    k.append(a)
v = 0
j = 1
p = 3
c = []
h = []
g = []
l = set()
for x in k:
    k[v][j] = int(k[v][j])
    k[v][p] = int(k[v][p])
    if k[v][j] > k[v][p]:
        j -= 1
        c.append(k[v][j])
        l.add(k[v][j])
        j += 1
        c.append(k[v][j])
        p -= 1
        g.append(k[v][p])
        l.add(k[v][p])
        p += 1
        g.append(k[v][p])

    elif k[v][j] < k[v][p]:
        j -= 1
        g.append(k[v][j])
        l.add(k[v][j])
        j += 1
        g.append(k[v][j])
        p -= 1
        c.append(k[v][p])
        l.add(k[v][p])
        p += 1
        c.append(k[v][p])
    elif k[v][j] == k[v][p]:
        j -= 1
        h.append(k[v][j])
        l.add(k[v][j])
        j += 1
        h.append(k[v][j])
        j += 1
        h.append(k[v][j])
        l.add(k[v][j])
        j += 1
        h.append(k[v][j])
        j -= 2
    v += 1
v = 0
b = []
while v < len(c):
    if v >= len(c):
        break
    if c[v] in b:
        v += 2
        continue
    s = c.count(c[v])
    b.append(c[v])
    b.append(s)
    v += 2
v = 0
y = []
while v < len(h):
    if v >= len(h):
        break
    if h[v] in y:
        v += 2
        continue
    s = h.count(h[v])
    y.append(h[v])
    y.append(s)
    v += 2
v = 0
p = []
while v < len(g):
    if v >= len(g):
        break
    if g[v] in p:
        v += 2
        continue
    s = g.count(g[v])
    p.append(g[v])
    p.append(s)
    v += 2

for x in l:
    ok = x
    zz = 0
    si = c.count(ok) + h.count(ok) + g.count(ok)
    print(ok, end='')
    print(':', end='')
    print(si, '', end='')
    if ok in b:
        mm = b.index(ok)
        mm += 1
        zz = b[mm] * 3
        print(b[mm], '', end='')
    else:
        print(0, '', end='')
    if ok in y:
        mm = y.index(ok)
        mm += 1
        zz += y[mm] * 1
        print(y[mm], '', end='')
    else:
        print(0, '', end='')
    if ok in p:
        mm = p.index(ok)
        mm += 1
        zz += 0
        print(p[mm], '', end='')
    else:
        print(0, '', end='')
    print(zz)
