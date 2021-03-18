'''
Условие задачи:
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''

#Code
import requests
with open('dataset_3378_3.txt','r') as b:
    s=b.readline().strip()
    r = requests.get(s)

e= requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
x=1
while x>0:
    if 'We' in e.text:
        with open('3378_answer.txt', 'w+') as v:
            v.write(e.text)
        break
    else:
        e = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + e.text)
        x+=1
