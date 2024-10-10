import numpy as np
import os


variant_number = 2

n = variant_number * 10
m = n - variant_number

A = np.random.normal(loc=0, scale=1, size=(n, m))
B = np.random.normal(loc=0, scale=1, size=(n, m))

min_A = np.min(A)
max_B = np.max(B)

sum_A = np.sum(A)

mean_B = np.mean(B)

A_multiplied = A * mean_B

sum_B_columns = np.sum(B, axis=0)

max_A_rows = np.max(A, axis=1)

product_AB = A @ B.T

A_flat = A.flatten()
B_flat = B.flatten()
C = np.column_stack((A_flat, B_flat))

output_file = '/home/nikita/Документы/neyro/teorneyro/results.txt'

with open(output_file, 'w') as f:
    f.write("Минимальное значение в A:{}\n".format (min_A))
    f.write("Максимальное значение в B:{}\n".format (max_B))
    f.write("Сумма всех элементов в A:{}\n".format (sum_A))
    f.write("Среднее значение всех элементов в B:{}\n".format (mean_B))
    f.write("Массив A, умноженный на среднее значение в B:\n{}\n".format (A_multiplied))
    f.write("Сумма всех элементов в B по столбцам:{}\n".format (sum_B_columns))
    f.write("Максимальное значение в A по строкам:{}\n".format (max_A_rows))
    f.write("Произведение A и B:\n{}\n".format (product_AB))
    f.write("Объединенный массив C:\n{}\n".format (C))

if os.path.exists(output_file):
    print(f"Результаты успешно записаны в файл: {output_file}")
else:
    print("Ошибка при записи в файл.")