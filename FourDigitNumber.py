def fourDigitNumber():
    print("Проверка четырехзначного числа")
    fourDigit = input("Введите четырехзначное число: ")
    summa = 0
    difference = 0
    if int(fourDigit)%3 == 0:
        summa += int(fourDigit[0])
        summa += int(fourDigit[1])
        summa += int(fourDigit[2])
        summa += int(fourDigit[3])
        print(summa)
    else:
        difference -= int(fourDigit[0])
        difference -= int(fourDigit[1])
        difference -= int(fourDigit[2])
        difference -= int(fourDigit[3])
        print(difference)
