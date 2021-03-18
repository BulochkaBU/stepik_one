'''
Условие задачи:
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
'''


#Code
with open('dataset_3363_2.txt') as g:
    a=g.readline()
k = 0
for x in a:
    k += 1
    if x >= 'A':
        n = ''
        b = x
        continue
    if x < 'A':
        n = n + x
    n = int(n)
    if n > 9:
        print(b * n, end='')
    if n <= 9:
        if k >= len(a):
            print(b * n, end='')
        elif a[k] >= 'A':
            print(b * n, end='')
        else:
            n = str(n)
            continue
    n = str(n)

with open('answer_3363_2.txt','w') as y:
    y.write('AKKKKKKKKKKKfffffyyyyyyyyyyyyyyyyyyyaaaaaaaaaaaaakkkkkzzzzzzzzzzzzzzzssssssssssssssssFFFFFFFFFFFFPPPPPPPPPPPPPPPPPGGGGGGGGGGGGBBWWWWZZZZZZZZZZZZZZZZZZMMMMMMMMMIIIIIIIIIIIIIIIaaaaaaaaaaaaayyyyyyyyyyyyyyXXXXXXXXXXXXXXXXXXXXddddddddddddcccccccccccccllllllllllZZZZZZZZZZZZDDDDDDDDDDDDDDDvvvvvvvvvvvcccccrrrrrFFFHHHHHHHHHHHTyyyyyyyyyyyyyySSSSSSooooooooooGGGGGGGGGBBDDDDDDDDDDDDDrrrhhhhhhhhhccc')