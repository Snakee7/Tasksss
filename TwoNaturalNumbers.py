def TwoNaturalNumbers():
    print("Действия над числами из условия")
    a = int(input("Введите значение для переменной а: "))
    b = int(input("Введтие значение для переменной b: "))
    firstValue = 0
    secondValue = 0
    if a%3 == 0 and b%3 == 0:
        firstValue = (a+b)/3
        print(firstValue)
    else:
        secondValue = (a+b)*3
        print(secondValue)
