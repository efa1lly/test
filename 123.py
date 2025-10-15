import numpy


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))


print("Введите элементы матрицы a:")
A = numpy.array([list(map(int, input(f"Строка {i+1}: ").split())) for i in range(rows)]


print("Матрица A:")
print(A)
