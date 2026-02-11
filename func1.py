flights = []
print("Введите данные о рейсах (пустой пункт назначения - завершение):")
while True:
    dest = input("\nПункт назначения: ").strip()
    if not dest:
        break
    try:
        num = int(input("Номер рейса: "))
        plane = input("Тип самолета: ").strip()

        if not plane:
            print("Ошибка: тип самолета не может быть пустым")
            continue
        flights.append({'dest': dest, 'num': num, 'plane': plane})
    except ValueError:
        print("Ошибка: номер рейса должен быть числом")
flights.sort(key=lambda x: x['num'])
if flights:
    search = input("\nВведите пункт назначения для поиска: ").strip()
    found = [f for f in flights if f['dest'].lower() == search.lower()]
    if found:
        print(f"\nРейсы в {search}:")
        for f in found:
            print(f"  №{f['num']} - {f['plane']}")
    else:
        print(f"Рейсов в {search} не найдено")
else:
    print("Нет данных о рейсах")