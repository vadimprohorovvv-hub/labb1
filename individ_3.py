n = int(input("Введите натуральное число n: "))
print(f"Натуральные делители числа {n}:")
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        c += 1
print(f"\nКоличество делителей: {c}")