n = float(input("Введите значение n: "))
k = n // 7
r = n % 7
if r == 0:
    print(f"7k = {7 * k}")
else:
    print(f"n = 7k + r = {7 * k} + {r} = {7 * k + r}")