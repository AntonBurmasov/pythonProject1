# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
#                 - 6 -> да
#                 - 7 -> да
#                 - 1 -> нет

print('Введите день недели для проверки, является ли он выходным.')
num = int(input())

if num > 5 and num < 8:
    print('Да.')



elif num > 0 and num < 6:
    print('Нет.')

else:
    print('Вводимое число должно быть больше 0 и меньше 8.')