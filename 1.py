def fixing_cords(number, planet, cords):
    # функция реализует работу формулы для исправления координат
    # number - номер корабля
    # planet - планета корабля
    # cords - координаты вектора направления
    n, m = number[5], number[-1]
    n = int(n)
    m = int(m)
    xd, yd = cords.split()
    xd = int(xd)
    yd = int(yd)
    t = len(planet)
    if n > 5:
        x = n + xd
    else:
        x = -(n + xd) * 4 + t
    if m > 3:
        y = m + t + yd
    else:
        y = -(n+yd) * m
    return str(x) + ' ' + str(y)


file = open('space.txt', encoding='utf-8')  # открыли файл
new_rows = []
header = file.readline()  # считали шапку
for i in range(100):  # ищем неисправности в каждой строке
    row = file.readline().split('*')
    coord_place1, coord_place2 = row[2].split()
    coord_place1 = int(coord_place1)
    coord_place2 = int(coord_place2)
    if coord_place1 == 0 and coord_place2 == 0:  # исправление найденной неисправности
        row[2] = fixing_cords(row[0], row[1], row[3])
    if i != 99:  # удаление символа переноса на следующую строку
        row[-1] = row[-1][:-1]
    # соединили все элементы звездочкой, как в изначальном файле
    new_rows.append('*'.join(row))

for st in new_rows:  # ищем строки в котрых последняя буква кода корабля равен V
    st = st.split('*')
    code = st[0]
    changed_cords = st[-2].split()
    cords_with_mark = str(changed_cords[0]) + ',' + str(changed_cords[1])
    if code[-5] == 'V':
        print(f'{code} - ({cords_with_mark})')

with open('space_new.txt', 'w', encoding='utf-8', newline='') as file1:  # запись в новый файл
    print(header, file=file1, end='')  # запись шапки
    for row in new_rows:  # запись каждой исправленной строки
        print(row, file=file1)
