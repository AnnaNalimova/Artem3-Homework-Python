"""
Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

a = input('Enter 6-digit number - ')
result = 'yes' if (int(a[0]) + int(a[1]) + int(a[2])) == (int(a[3]) + int(a[4]) + int(a[5])) else 'no'
print(f'{a} -> {result}')