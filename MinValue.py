def minValue():
    print("Нахождение минимального значения из введенных чисел")
    a = int(input("Введите значение для переменной a:"))
    b = int(input("Введите значение для переменной b:"))
    c = int(input("Введите значение для переменной c:"))

    if a<b<c:
        print("Минимально значение a: ", a)
    elif b<a<c:
        print("Минимально значение b: ", b)
    elif c<a<b:
        print("Минимально значение c: ", c)
    else:
        print("Произошла ошибка")
