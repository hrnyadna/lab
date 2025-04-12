##1 вариант
month = int(input('Введите количество месяцев:'))
pari = int(input('Введите количество рождающихся кроликов у одной пары:'))
month1, month2 = 1, 1
for i in range(3, month + 1):
    month1, month2 = month2, month2 + month1 * pari

print(month2)