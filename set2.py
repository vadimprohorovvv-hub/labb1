def main():
    flights = []

    print("=== Ввод данных о рейсах ===")
    print("Для завершения ввода введите 'exit' в названии пункта назначения")
    print()
    while True:
        print(f"Рейс #{len(flights) + 1}")

        destination = input("Пункт назначения: ").strip()
        if destination.lower() == 'exit':
            if len(flights) == 0:
                print("Не введено ни одного рейса!")
                return
            break

        try:
            flight_num = int(input("Номер рейса: ").strip())
        except ValueError:
            print("Ошибка! Номер рейса должен быть числом. Попробуйте еще раз.")
            continue

        aircraft_type = input("Тип самолета: ").strip()
        if not destination or not aircraft_type:
            print("Ошибка! Все поля должны быть заполнены. Попробуйте еще раз.")
            continue
        flight_data = {
            'destination': destination,
            'flight_number': flight_num,
            'aircraft_type': aircraft_type
        }

        flights.append(flight_data)
        print(f"Рейс добавлен! Всего рейсов: {len(flights)}\n")
    flights.sort(key=lambda x: x['flight_number'])

    print("\n=== Список всех рейсов (отсортирован по номеру) ===")
    print("№\tНомер рейса\tПункт назначения\tТип самолета")
    print("-" * 60)

    for i, flight in enumerate(flights, 1):
        print(f"{i}\t{flight['flight_number']}\t\t{flight['destination']:20}\t{flight['aircraft_type']}")
    print("\n" + "=" * 60)
    print("=== Поиск рейсов по пункту назначения ===")

    while True:
        search_dest = input("\nВведите пункт назначения для поиска (или 'exit' для выхода): ").strip()

        if search_dest.lower() == 'exit':
            break

        if not search_dest:
            print("Ошибка! Введите пункт назначения.")
            continue
        found_flights = []
        for flight in flights:
            if flight['destination'].lower() == search_dest.lower():
                found_flights.append(flight)
        if found_flights:
            print(f"\nНайдено рейсов в '{search_dest}': {len(found_flights)}")
            print("Номер рейса\tТип самолета")
            print("-" * 30)

            for flight in found_flights:
                print(f"{flight['flight_number']:12}\t{flight['aircraft_type']}")
        else:
            print(f"\nРейсов в пункт назначения '{search_dest}' не найдено.")
        print(f"\nВсего в базе: {len(flights)} рейсов")
        print(f"Найдено: {len(found_flights)} рейсов")


if __name__ == "__main__":
    main()