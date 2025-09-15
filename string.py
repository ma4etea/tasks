

print("({})-{}-{}".format(*{1, 2, 3}))

print("({a})-{b}-{c}".format(**{"a": 3, "b": 4, "c": 6}))


class CustomDict(dict):
    """
    Здравствуйте, Анна!
    Ваш заказ №48392 ожидает отправки.
    Город доставки: <нет данных>.
    """
    def __missing__(self, key):
        return "<нет данных>"

def render_template(template_: str, context_: dict):
    return template_.format_map(CustomDict(context_))


template = "Здравствуйте, {name}!\nВаш заказ №{order_id} ожидает отправки.\nГород доставки: {city}."
context = {"name": "Анна", "order_id": 48392}
print(render_template(template, context))



