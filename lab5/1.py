import numpy as np

zero_vec = np.zeros(10)
print(zero_vec)

filled_vec = np.full(10,2.5)
print(filled_vec)

zero_vec[4] =1
print(zero_vec)

arange_vec = np.arange(10,50)
print(arange_vec)

quest_vec = np.array([1,2,0,0,4,0])
print(*quest_vec.nonzero())


eye_matrix = np.eye(3,3)
print(eye_matrix)


random_matrix = np.random.rand(10,10)
print(random_matrix.max(), ' ',random_matrix.min())

random_vec = np.random.rand(1,30)
print(random_vec.mean())


chess = np.zeros((8, 8), dtype=int)
chess[1::2, ::2] = 1
chess[::2, 1::2] = 1
print("Шахматная матрица 8x8:")
print(chess, "\n")


A = np.random.randint(1, 10, (5, 3))
B = np.random.randint(1, 10, (3, 2))
C = np.dot(A, B)
print("Матрица A (5x3):")
print(A)
print("Матрица B (3x2):")
print(B)
print("Результат перемножения (5x2):")
print(C, "\n")


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr3 = np.array([1, 3, 2])
print("arr1 и arr2 одинаковы?", np.array_equal(arr1, arr2))
print("arr1 и arr3 одинаковы?", np.array_equal(arr1, arr3), "\n")


arr = np.random.randint(0, 100, (4, 4))
print("Исходный массив:")
print(arr)
arr[arr == np.max(arr)] = 0
print("После замены максимального элемента на 0:")
print(arr, "\n")


arr = np.random.randint(0, 10, 20)
values, counts = np.unique(arr, return_counts=True)
most_common = values[np.argmax(counts)]
print("Массив:", arr)
print("Наиболее частое значение:", most_common, "\n")


arr = np.random.randint(0, 100, 15)
n = 3
largest = np.sort(arr)[-n:]
print("Массив:", arr)
print(f"{n} наибольших значения:", largest)