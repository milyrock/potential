file = open('space.txt', encoding='utf-8')  # открыли файл
text = []
first = []
number = ''
header = file.readline()  # считали шапку

for i in range(100):  # сосчитали все строки
    row = file.readline().split('*')
    first.append(row)
    number = ''
    for ch in row[0]:  # выбор цифр из кода корабля
        if ch in '0123456789':
            number += str(ch)
    if i != 99:  # удаление символа переноса на следующую строку
        row[-1] = row[-1][:-1]
    row[0] = number
    text.append(row)


for i in range(len(text)):
    key = text[i]
    j = i - 1
    while int(text[j][0]) < int(key[0]) and j > 0:
        text[j+1] = text[j]
        j -= 1
    text[j+1] = key

top_ten = []
cnt = 0

for row in text:
    top_ten.append(row[0])
    cnt += 1
    if cnt == 11:
        break

for numero in top_ten:
    for row in first:
        if str(numero) in row[0] and numero != str(302):
            print('*'.join(row))
