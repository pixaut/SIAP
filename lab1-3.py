numbers = list(map(int,input().split()))

result = 1
for i in range(1,len(numbers),2):
    result *= numbers[i] 

numbers.remove(max(numbers))
print(f'Произведение чисел на чётных номерах: {result}')
print(f'Длина списка: {len(numbers)}' )