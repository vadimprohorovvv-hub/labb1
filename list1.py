A = [float(input(f"Элемент {i + 1}: ")) for i in range(10)]
sum_negative = sum(num for num in A if num < 0)
print(f"\nВведенный список: {A}")
print(f"Сумма отрицательных элементов: {sum_negative}" if sum_negative < 0 else "Отрицательных элементов нет")