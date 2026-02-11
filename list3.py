tuple_input = input("Введите элементы кортежа через пробел: ")
T = tuple(tuple_input.split())
print(f"Кортеж: {T}")
found = False
pair_indices = ()

for i in range(len(T) - 1):
    if T[i] == T[i + 1]:
        found = True
        pair_indices = (i, i + 1)
        break
if found:
    print(f"\nНайдена пара одинаковых соседних элементов!")
    print(f"Элементы: {T[pair_indices[0]]} и {T[pair_indices[1]]}")
    print(f"Их индексы (номера): {pair_indices[0]} и {pair_indices[1]}")
    print(f"Позиции в кортеже (начиная с 1): {pair_indices[0] + 1} и {pair_indices[1] + 1}")
else:
    print("\nПар одинаковых соседних элементов не найдено.")