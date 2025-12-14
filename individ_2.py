a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(f"\nПо возрастанию: {a}, {b}, {c}")
print(f"По убыванию: {c}, {b}, {a}")