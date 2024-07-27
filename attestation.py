from modules import plus, minus, muliply, division

result = 0
numO = 0
numT = 0
act = 0

print("Добро пожаловать в мой калькулятор!")

while True:
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("0.Выход")
    act = int(input('Введите действие:'))
    if act == 1:
        numO = int(input("Введите первое число:"))
        numT = int(input("Введите второе число:"))
        result = plus(numO,numT)
        print(f"Сумма равна: {result}")
    elif act == 2:
        numO = int(input("Введите первое число:"))
        numT = int(input("Введите второе число:"))
        result = minus(numO,numT)
        print(f"Разность равна: {result}")
    elif act == 3:
        numO = int(input("Введите первое число:"))
        numT = int(input("Введите второе число:"))
        result = muliply(numO,numT)
        print(f"Произведение равно: {result}")
    elif act == 4:
        numO = int(input("Введите первое число:"))
        numT = int(input("Введите второе число:"))
        result = division(numO,numT)
        print(f"Частное равно: {result}")
    elif act == 0:
        print("Выход из калькулитара")
        break

