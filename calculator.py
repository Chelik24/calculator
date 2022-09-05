Again = 'yes'
while Again == 'yes':
    num = float(input("Введите число_"))
    op = input("Введите знак_")
    num2 = float(input("Введите число_"))
    if op == '+':
     print(num + num2)
    elif op == '-':
     print(num - num2)
    elif op == '*':
        print(num * num2)
    elif op == '/':
        print(num / num2)
    else:
        print("Ошибка!!!")
    Again = input('Введите "yes" если хотите продолжить или "no" если хотите закончить_')
'Боже как делать дизайн'

