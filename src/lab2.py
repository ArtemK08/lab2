# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 4 (впишіть свій варіант)
# ПІБ: Коваленк Артем (впишіть своє ПІБ)

# Тут має бути Ваш код
# Набір даних (20 елементів)
car_services = [
    {"id": 1, "name": "Заміна моторного масла", "mileage_interval": 10000, "cost": 2500},
    {"id": 2, "name": "Заміна масляного фільтра", "mileage_interval": 10000, "cost": 400},
    {"id": 3, "name": "Заміна повітряного фільтра", "mileage_interval": 15000, "cost": 600},
    {"id": 4, "name": "Заміна салонного фільтра", "mileage_interval": 15000, "cost": 500},
    {"id": 5, "name": "Заміна паливного фільтра", "mileage_interval": 30000, "cost": 1200},
    {"id": 6, "name": "Заміна свічок запалювання", "mileage_interval": 30000, "cost": 1800},
    {"id": 7, "name": "Заміна гальмівної рідини", "mileage_interval": 40000, "cost": 900},
    {"id": 8, "name": "Заміна охолоджуючої рідини (антифризу)", "mileage_interval": 50000, "cost": 1500},
    {"id": 9, "name": "Заміна ременя ГРМ з роликами", "mileage_interval": 60000, "cost": 4500},
    {"id": 10, "name": "Заміна гальмівних колодок (передніх)", "mileage_interval": 30000, "cost": 2000},
    {"id": 11, "name": "Заміна гальмівних колодок (задніх)", "mileage_interval": 40000, "cost": 2000},
    {"id": 12, "name": "Заміна гальмівних дисків", "mileage_interval": 80000, "cost": 5000},
    {"id": 13, "name": "Діагностика підвіски", "mileage_interval": 15000, "cost": 600},
    {"id": 14, "name": "Регулювання розвалу-сходження", "mileage_interval": 20000, "cost": 800},
    {"id": 15, "name": "Чистка дросельної заслінки", "mileage_interval": 40000, "cost": 700},
    {"id": 16, "name": "Заміна масла в КПП", "mileage_interval": 50000, "cost": 2200},
    {"id": 17, "name": "Заміна щіток склоочисника", "mileage_interval": 20000, "cost": 500},
    {"id": 18, "name": "Заправка кондиціонера", "mileage_interval": 30000, "cost": 1200},
    {"id": 19, "name": "Перевірка акумулятора", "mileage_interval": 20000, "cost": 300},
    {"id": 20, "name": "Комп'ютерна діагностика систем", "mileage_interval": 15000, "cost": 800}
]

#  1. Звичайні функції
def calculate_remaining_mileage(current_mileage: int, last_service_mileage: int, interval: int) -> int:
    """Розраховує залишок пробігу до наступного обслуговування."""
    next_service = last_service_mileage + interval
    return next_service - current_mileage

def format_service_info(service_name: str, cost: float) -> str:
    """Форматує рядок із назвою послуги та її вартістю."""
    return f"Послуга: {service_name} | Вартість: {cost:.2f} грн"


#  2. Функція з параметрами за замовчуванням
def calculate_service_cost_with_tax(base_cost: float, discount_percent: float = 0.0, tax_rate: float = 0.0) -> float:
    """Розраховує кінцеву вартість послуги з урахуванням знижки та податку за замовчуванням."""
    discounted = base_cost * (1 - discount_percent / 100)
    final_cost = discounted * (1 + tax_rate / 100)
    return round(final_cost, 2)


#  3. Функція зі змінною кількістю аргументів (*args)
def total_additional_expenses(*expenses: float) -> float:
    """Обчислює суму довільної кількості додаткових непередбачуваних витрат."""
    return sum(expenses)


#  4. Лямбда-функція
# Розраховує вартість зі знижкою
apply_discount = lambda cost, percent: round(cost * (1 - percent / 100), 2)


#  5. Рекурсивна функція
def calculate_projected_cost(years: int, base_cost: float, annual_inflation: float) -> float:
    """Рекурсивно обчислює прогнозовану вартість обслуговування за N років з урахуванням інфляції."""
    if years <= 0:
        return 0.0
    if years == 1:
        return base_cost
    # Рекурсивний випадок: вартість поточного року + наступний рік з урахуванням інфляції
    return base_cost + calculate_projected_cost(years - 1, base_cost * (1 + annual_inflation / 100), annual_inflation)


#  6. Функції вищого порядку та функціональне програмування
def apply_to_services(services: list, func: callable) -> list:
    """Приймає іншу функцію як аргумент та застосовує її до кожного елемента списку (функція вищого порядку)."""
    return [func(item) for item in services]

def filter_budget_services(services: list, max_cost: float) -> list:
    """Використовує вбудовану функцію filter для відбору бюджетних послуг."""
    return list(filter(lambda s: s['cost'] <= max_cost, services))


#  7. Інтерактивна програма (меню)
def main():
    print("Вітаємо в системі планування технічного обслуговування автомобіля")

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Переглянути список усіх послуг та регламенту")
        print("2. Розрахувати залишок пробігу до обслуговування")
        print("3. Обчислити вартість послуги з урахуванням знижки/податку (з параметрами за замовчуванням)")
        print("4. Порахувати суму додаткових витрат (*args)")
        print("5. Прогнозувати вартість обслуговування на кілька років (рекурсія)")
        print("6. Фільтрувати бюджетні послуги")
        print("7. Застосувати функцію вищого порядку (форматування даних)")
        print("8. Вийти")

        try:
            choice = int(input("Оберіть пункт меню (1-8): "))

            if choice == 1:
                print("\nСписок послуг:")
                for s in car_services:
                    print(f"[{s['id']}] {s['name']} — Інтервал: {s['mileage_interval']} км — Ціна: {s['cost']} грн")

            elif choice == 2:
                current = int(input("Введіть поточний пробіг авто (км): "))
                last = int(input("Введіть пробіг на момент останнього ТО (км): "))
                interval = int(input("Введіть регламентний інтервал послуги (км): "))
                remaining = calculate_remaining_mileage(current, last, interval)
                if remaining > 0:
                    print(f"До наступного обслуговування залишилось: {remaining} км.")
                else:
                    print(f"Увага! Обслуговування протерміновано на {abs(remaining)} км!")

            elif choice == 3:
                cost = float(input("Введіть базову вартість послуги (грн): "))
                disc_input = input("Введіть знижку у % (натисніть Enter для значення за замовчуванням 0): ")
                disc = float(disc_input) if disc_input else 0.0
                tax_input = input("Введіть податок у % (натисніть Enter для значення за замовчуванням 0): ")
                tax = float(tax_input) if tax_input else 0.0

                final = calculate_service_cost_with_tax(cost, disc, tax)
                print(f"Кінцева вартість послуги: {final} грн")

            elif choice == 4:
                raw_exp = input("Введіть додаткові витрати через пробіл (наприклад: 300 1500 450): ")
                expenses = [float(x) for x in raw_exp.split()]
                total = total_additional_expenses(*expenses)
                print(f"Загальна сума додаткових витрат: {total} грн")

            elif choice == 5:
                years = int(input("Введіть кількість років для прогнозу: "))
                base = float(input("Базова річна вартість обслуговування (грн): "))
                inflation = float(input("Рівень інфляції на рік (%): "))
                projected = calculate_projected_cost(years, base, inflation)
                print(f"Прогнозована сукупна вартість за {years} років: {projected:.2f} грн")

            elif choice == 6:
                limit = float(input("Введіть максимальну вартість для бюджетних послуг (грн): "))
                budget_list = filter_budget_services(car_services, limit)
                print(f"\nЗнайдено послуг ( <= {limit} грн ): {len(budget_list)}")
                for s in budget_list:
                    print(f"- {s['name']} ({s['cost']} грн)")

            elif choice == 7:
                formatted = apply_to_services(car_services[:5], lambda s: format_service_info(s['name'], s['cost']))
                print("\nРезультат роботи функції вищого порядку (перші 5 послуг):")
                for item in formatted:
                    print(item)

            elif choice == 8:
                print("Дякуємо за використання програми! До побачення.")
                break
            else:
                print("Невірний вибір. Будь ласка, оберіть число від 1 до 8.")
        except ValueError:
            print("Помилка вводу. Перевірте правильність введених даних.")

if __name__ == "__main__":
    main()

# Не забувайте форматувати вивід та додавати коментарі!
