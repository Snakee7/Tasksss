import DepartmentMenu
import MinValue
import TwoNaturalNumbers
import TwoNegativeNumbers
import FourDigitNumber

MenuDepartmentMenu = '1'
MenuMinValue = '2'
MenuFourDigitNumber = '3'
MenuTwoNaturalNumbers = '4'
MenuTwoNegativeNumbers = '5'

print(
'''
Меню:
1. Выбираем из представленных пунктов нужный
2. Находим минимальное значение из введенных чисел
3. Выполняем действие над четырехзначном числе с условием: Если число кратно тремб то вычислится сумма цифр этого числа, иначе-произведение 
4. Выволняем действия с двумя натуральными числами
5. Вычисление двух вещественных чисел с условием: Если хотя бы одно число будет отрицательное то выполняется вычисление средне арифметическое,иначе - средне геометрическое
(Наберите номер пункта и нажмите <ENTER>)
'''
)

menu_value = input()
if      menu_value == MenuDepartmentMenu:
    DepartmentMenu.departmentMenu()
elif    menu_value == MenuMinValue:
    MinValue.minValue()
elif    menu_value == MenuFourDigitNumber:
    FourDigitNumber.fourDigitNumber()
elif    menu_value == MenuTwoNaturalNumbers:
    TwoNaturalNumbers.TwoNaturalNumbers()
elif    menu_value == MenuTwoNegativeNumbers:
    TwoNegativeNumbers.TwoNegativeNumbers()
else:
    print("Неверные данные!")

input("Нажмите <ENTER> для выхода")    
