from collections import defaultdict

orders = [
    ("Анна", 2500),
    ("Борис", 1800),
    ("Анна", 3400),
    ("Дмитрий", 500),
    ("Борис", 1200),
    ("Анна", 1000),
]


def group_orders_by_user(orders_: list[tuple[str, int]]) -> dict[str, list[int]]:
    """
            Напиши функцию, которая возвращает словарь, где ключ — имя пользователя,
            а значение — список всех его сумм заказов.
        {
        "Анна": [2500, 3400, 1000],
        "Борис": [1800, 1200],
        "Дмитрий": [500]
        }
    """
    user_orders_map = defaultdict(list)
    for order in orders_:
        user_orders_map[order[0]].append(order[1])
    return dict(user_orders_map)


print(group_orders_by_user(orders))

purchases = [
    ("еда", 500),
    ("техника", 30000),
    ("одежда", 2500),
    ("еда", 700),
    ("техника", 12000),
    ("еда", 300),
]


def sum_by_category(purchases_: list[tuple[str, int]]) -> dict[str, int]:
    """
    Напиши функцию sum_by_category(purchases: list[tuple[str, int]]) -> dict[str, int],
    которая вернёт словарь, где ключ — категория,
    а значение — суммарные расходы по этой категории.

    вывод:
    {
    "еда": 1500,
    "техника": 42000,
    "одежда": 2500
    }
    """

    purchases_amount_map = defaultdict(int)

    for purchase in purchases_:
        purchases_amount_map[purchase[0]] += purchase[1]
    return dict(purchases_amount_map)


print(sum_by_category(purchases))


def unique_cities_by_user(visits: list[tuple[str, str]]) -> dict[str, set[str]]:
    """
        visits = [
        ("Анна", "Москва"),
        ("Борис", "Питер"),
        ("Анна", "Казань"),
        ("Анна", "Москва"),
        ("Дмитрий", "Питер"),
        ("Борис", "Москва"),
        ("Дмитрий", "Казань"),
        ]

        Напиши функцию unique_cities_by_user(visits: list[tuple[str, str]]) -> dict[str, set[str]],
        - которая вернёт словарь,
        — где ключ — имя пользователя,
        — а значение — множество уникальных городов, которые он посетил.
        🔹 Ожидаемый результат:

        {
            "Анна": {"Москва", "Казань"},
            "Борис": {"Питер", "Москва"},
            "Дмитрий": {"Питер", "Казань"}
        }

    """
    user_visits_map = defaultdict(set[str])
    for visit in visits:
        user_visits_map[visit[0]].add(visit[1])

    return dict(user_visits_map)


print(unique_cities_by_user([("Анна", "Москва"),
                       ("Борис", "Питер"),
                       ("Анна", "Казань"),
                       ("Анна", "Москва"),
                       ("Дмитрий", "Питер"),
                       ("Борис", "Москва"),
                       ("Дмитрий", "Казань"), ]))
