from logger import input_data, print_data

def interface(): 
    print("Добрый день, вы попали на специальный бот-справочник от GeekBrains! \n 'Варианты услуг:' \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число: '))

    while command != 1 and command != 2: 
        print('Число введено неверно, ознакомьтесь с вариантами услуг')
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
