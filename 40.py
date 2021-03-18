'''
Условие задачи:
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте.

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

#Code
with open('dataset_3380_5.txt') as i:
    a=i.read().strip().split()
v=1
b=2
w=0
s=[]
for x in a:
    if v>=len(a):
        break
    del a[v]
    v+=2
for x in a:
    k=x
    k=int(k)
    s.append(k)
h=[]
f=0
for x in s:
    if f>=len(s):
        break
    h.append(s[f])
    f+=2
h.sort()
j=0
for x in h:
    if j>=len(h):
        break
    while h.count(h[j])!=1:
        del(h[j])
    j+=1
t=0
y=1
g,q,w,e,u,i,o,p,z,xx,cc=[],[],[],[],[],[],[],[],[],[],[]
for x in s:
    if t>=len(s):
        break
    if y>=len(s):
        break
    if s[t]==1:
        g.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==2:
        q.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==3:
        w.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==4:
        e.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==5:
        u.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==6:
        i.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==7:
        o.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==8:
        p.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==9:
        z.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==10:
        xx.append(s[y])
        t+=2
        y+=2
        continue
    if s[t]==11:
        cc.append(s[y])
        t+=2
        y+=2
        continue
    else:
        t+=2
        y+=2
n=0
for x in h:
    ok=x
    if ok in s:
        if ok==1:
            print(h[n], '', sum(g) / s.count(h[n]))
            n+=1
        if ok==2:
            print(h[n], '', sum(q) / s.count(h[n]))
            n += 1
        if ok==3:
            print(h[n], '', sum(w) / s.count(h[n]))
            n += 1
        if ok==4:
            print(h[n], '', sum(e) / s.count(h[n]))
            n += 1
        if ok == 5:
            print(h[n], '', sum(u) / s.count(h[n]))
            n += 1
        if ok==6:
            print(h[n], '', sum(i) / s.count(h[n]))
            n += 1
        if ok==7:
            print(h[n], '', sum(o) / s.count(h[n]))
            n += 1
        if ok==8:
            print(h[n], '', sum(p) / s.count(h[n]))
            n += 1
        if ok==9:
            print(h[n], '', sum(z) / s.count(h[n]))
            n += 1
        if ok==10:
            print(h[n], '', sum(xx) / s.count(h[n]))
            n += 1
        if ok==11:
            print(h[n], '', sum(cc) / s.count(h[n]))
            n += 1
    else:
        print(h[n], '', '-')
        n += 1


