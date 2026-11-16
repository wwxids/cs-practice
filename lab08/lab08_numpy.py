import numpy as np

#1

hours = np.arange(0, 22, 3)


line = np.linspace(0, 1, 5)

zeros = np.zeros(6, dtype=int)

unknown_table = np.full((2, 3), -1)

identity = np.eye(3)

print("hours:", hours)
print("hours.shape:", hours.shape)
print("hours.ndim:", hours.ndim)
print("hours.size:", hours.size)
print("hours.dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros, "dtype:", zeros.dtype)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

#2


print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

#3
print("\n" + "=" * 50)
print("Задание 3. Строки и столбцы таблицы")
print("=" * 50)

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

#4

matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная matrix:\n", matrix)

first_three = matrix[:3]
print("\nПервые три строки:\n", first_three, "\nshape:", first_three.shape)

last_two = matrix[-2:]
print("\nПоследние две строки:\n", last_two, "\nshape:", last_two.shape)

first_two_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_two_cols, "\nshape:", first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print("\nФрагмент строк 1–3, столбцов 2–4:\n", fragment, "\nshape:", fragment.shape)

corner = matrix[-2:, -2:]
print("\nУгловой блок 2×2 (правый нижний):\n", corner, "\nshape:", corner.shape)

#5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после замены:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после замены:\n", small_matrix)


changed_hours = hours.copy()
changed_hours[2:5] = 99          # индексы 2–4
changed_hours[0::2] = -1         # каждый второй, начиная с первого (индексы 0, 2, 4, 6)
print("\nchanged_hours:", changed_hours)
print("исходный hours:", hours)


changed_matrix = matrix.copy()
changed_matrix[1, :] = 0         # вторая строка → нули
changed_matrix[:, -1] = -1       # последний столбец → -1
changed_matrix[1:4, 1:4] = 100   # центральный блок 3×3 → 100
print("\nchanged_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

#6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)





