numbers = input('Введите число')

numbers_sum = sum(int(digit) for digit in numbers if int(digit)%2 == 1)

print(f'Сумма чисел: {numbers_sum}')