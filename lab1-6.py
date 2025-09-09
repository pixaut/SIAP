set1 = set(map(int,input('Введите первое множество: ').split()) )
set2 = set(map(int,input('Введите второе множество: ').split()) )

print(*(set1 & set2) )