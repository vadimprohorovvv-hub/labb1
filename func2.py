def report(title, *sections, **options):
    if options.get('upper', False):
        title = title.upper()

    separator = options.get('separator', '\n')
    result = f"=== {title} ===\n"

    for i, section in enumerate(sections, 1):
        result += f"{i}. {section}"
        if i < len(sections):
            result += separator

    return result
if __name__ == "__main__":
    print("Пример 1 (из задания):")
    print(report("Ежедневный отчет", "Продажи выросли", "Новых клиентов: 3", separator="\n---\n", upper=True))

    print("\n" + "=" * 50 + "\n")
    print("Пример 2 (без параметров, разделитель по умолчанию):")
    print(report("Еженедельный обзор", "Задача 1 выполнена", "Задача 2 в процессе", "Встреча запланирована"))

    print("\nПример 3 (с заглавным заголовком):")
    print(report("Ежемесячный анализ", "Доход увеличился", "Расходы стабильны", upper=True))

    print("\nПример 4 (с пользовательским разделителем):")
    print(report("Статус проекта",
                 "Фаза проектирования завершена",
                 "Разработка начата",
                 "Тестирование запланировано",
                 separator="\n" + "-" * 30 + "\n"))

    print("\nПример 5 (только заголовок):")
    print(report("Пустой отчет"))