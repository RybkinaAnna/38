from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n"
                     f"1 вариант: \n"
                     f"{name}\n {surname}\n{phone}\n{address}\n\n"
                     f"2 вариант \n"
                     f"{name};{surname};{phone};{address}\n"
                     f"Выберите вариант:"))
    
while var != 1 and var != 2: 
    print('Число введено неверно, ознакомьтесь с вариантами услуг')
    var = int(input('Введите число: '))
    if var == 1:
        with open('first.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2: 
        with open('second.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('first.csv', 'r', encoding = 'utf-8') as f:
        first = f.readlines()
        first_list = []
        j = 0
        for i in range (len(first)):
            if first[i] == '\n' or i == len(first) - 1:
                first_list(''.join(first[j:i+1]))
                j = i
        print(''.join(first_list))


              
print('Вывожу данные из второго файла: \n')
with open('seceond.csv', 'r', encoding = 'utf-8') as f:
    second = f.readlines
    ptint(second)
