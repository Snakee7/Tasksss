def departmentMenu():
     print("Выберите какой пункт вам нужен: ")
     while True:
        print("1. Кафедра ТК:")
        print("2. Факультет ФИСТ")
        print("3. Каферда Радиотехника")
        print("4. Выйти из программы")
        cmd = input("Выберите пункт: ")

        if cmd == "1":
            print("Выбран 1 пункт меню")
        elif cmd == "2":
            print("Выбран 2 пункт меню")
        elif cmd == "3":
            print("Выбран 3 пункт меню")
        elif cmd == "4":
            break
        else:
            print("Такой пункт не найден")
