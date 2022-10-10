def TwoNegativeNumbers():
    print("Вычисление среднее арифметическое или геометрическое значение")
    a = int(input("Введите значение для переменной а: "))
    b = int(input("Введтие значение для переменной b: "))
    arithmeticMean = 0
    geometricMean = 0
    if a>0 and b>0:
        arithmeticMean = (a+b)*2
        print(arithmeticMean)
    else:
        geometricMean = a*b
        print(geometricMean)
