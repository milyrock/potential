file = open('space.txt', encoding='utf-8')  # открыли файл
header = file.readline()
text = file.readlines()
name = input()
while name != "стоп":  # ввод строки
    for row in text:
        row = row.split('*')
        if not (row[-1][-1] in '0123456789'):
            row[-1] = row[-1][:-1]
        if name in row[0]:  # нашли строку содержащую нужный код корабля
            print(
                f'Корабль {row[0]} был отправлен с планеты: {row[1]} и его направление движения было: {row[-1]}')
            break
    else:
        print('error.. er.. ror..')
    name = input()
