A = {'a', 'b', 'h', 'j', 'l'}
B = {'b', 'c', 'h', 'l', 'r', 'v'}
C = {'j', 'k', 'n', 't', 'z'}
D = {'b', 'i', 'k', 'v', 'w'}
X = (A | B) & C
U = A | B | C | D
B_complement = U - B
Y = (A & B_complement) - (C | D)
print(f"X = {X}")
print(f"Y = {Y}")
print("\nДетализация:")
print(f"A ∪ B = {A | B}")
print(f"(A ∪ B) ∩ C = {X}")
print()
print(f"Универсальное множество U = {U}")
print(f"¬B = U \\ B = {B_complement}")
print(f"A ∩ ¬B = {A & B_complement}")
print(f"C ∪ D = {C | D}")
print(f"Y = (A ∩ ¬B) \\ (C ∪ D) = {Y}")