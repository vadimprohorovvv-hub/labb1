n = int(input("Введите количество элементов списка: "))
A = []
for i in range(n):
    element = float(input(f"Введите элемент {i + 1}: "))
    A.append(element)

print(f"\nИсходный список: {A}")
sum_odd_indices = 0
for i in range(1, len(A), 2):
    sum_odd_indices += A[i]
print(f"1. Сумма элементов с нечетными номерами: {sum_odd_indices}")
first_negative = -1
last_negative = -1

for i in range(len(A)):
    if A[i] < 0:
        first_negative = i
        break

for i in range(len(A) - 1, -1, -1):
    if A[i] < 0:
        last_negative = i
        break

sum_between = 0
if first_negative != -1 and last_negative != -1 and first_negative != last_negative:
    start = min(first_negative, last_negative) + 1
    end = max(first_negative, last_negative)

    for i in range(start, end):
        sum_between += A[i]

    print(f"2. Сумма между первым и последним отрицательными элементами: {sum_between}")
    print(f"   (между элементами с индексами {first_negative} и {last_negative})")
else:
    print(f"2. Нет двух разных отрицательных элементов")
compressed_list = []
count_removed = 0

for num in A:
    if abs(num) > 1:
        compressed_list.append(num)
    else:
        count_removed += 1
compressed_list.extend([0] * count_removed)

print(f"\n3. Сжатый список: {compressed_list}")
print(f"   Удалено элементов (|x| ≤ 1): {count_removed}")