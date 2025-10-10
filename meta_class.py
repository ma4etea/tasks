class MyMeta(type):
    def __new__(mcs, name, bases, attrs): # Здесь можно препарировать класс
        print(f"[MyMeta.__new__] Создаём класс {name}")
        return super().__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, **kwargs): # Здесь можно препарировать экземпляр
        print(f"[MyMeta.__call__] Создаём экземпляр класса {cls.__name__}")
        return super().__call__(*args, **kwargs)


# Класс, который использует метакласс
class Foo(metaclass=MyMeta):
    def __init__(self, value):
        print("[Foo.__init__] Инициализируем экземпляр")
        self.value = value


print("=== Объявление класса прошло ===")
print("Создаём объект...")
obj = Foo(42)





