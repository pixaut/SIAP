
dict = {
    'перстень': ['золото',200, 2],
    'подвеска': ['серебро',130, 3],
    'кольцо': ['золото',500, 1],
    'серьги': ['керамика, серебро',50, 5],
    'обруч': ['золото',1200, 2],
}


while True:
    print('1. Просмотр описания')
    print('2. Просмотр цены')
    print('3. Просмотр количества')
    print('4. Всю информацию')
    print('5. Покупка')
    print('6. До свидания')

    i = int(input('Ваш выбор '))
    if i == 1:
        
        name = input('Введите название изделия ')
        if not name in dict:
            print('Такого изделия нету')
        else:
            print(dict[name][0])

    elif i == 2:

        name = input('Введите название изделия ')
        if not name in dict:
            print('Такого изделия нету')
        else:
            print(dict[name][1])

    elif i == 3:

        name = input('Введите название изделия ')
        if not name in dict:
            print('Такого изделия нету')
        else:
            print(dict[name][2])

    elif i == 4:
        
        for item in dict.items():
            name, defin = item
            print(f'{name} : материал={defin[0]}, цена={defin[1]}, кол-во={defin[2]}')
            

    elif i == 5:
        name = input('Введите название изделия ')
        if not name in dict:
            print('Такого изделия нету')
        else:
            n = int(input('Сколько вы хотите купить?') )

            if dict[name][2] < n:
                print('В магазине нету столько изделий')
            else:
                dict[name][2] -= n
                print(f'Общая цена: {n*dict[name][1]}, в магазине осталось: {dict[name][2]}')
                print(f'Вы купили {name}, кол-во: {n}, на общую сумму: {n*dict[name][1]}')

    elif i == 6:
        print('До свидания')
        break
    else:
        print('Нет такого выбора')

    input('Нажмите для продолжения')
