correct_answer = 4 * 100 - 54
user_answer = input("Решите пример: 4 * 100 - 54 = ")
try:
    user_answer = int(user_answer)
except ValueError:
    print("Ошибка! Введите целое число.")
    exit()
print(f"Правильный ответ: {correct_answer}")
print(f"Ваш ответ: {user_answer}")
if user_answer == correct_answer:
    print("Правильно")
else:
    print("Неправильно")