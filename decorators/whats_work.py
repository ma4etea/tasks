
def test (decorator_args: str):
    print(f"test:{locals()=}")
    def decorator(func):
        print(f"decorator:{locals()=}")
        def wrapper(*args, **kwargs):
            print(f"Добавим в замыкание: {decorator_args=},а built он не замыкает так как они всегда доступны везде:{print=}")
            print(f"wrapper:{locals()=}")
            print(f"{func(*args, **kwargs)=}")
        return wrapper
    return decorator


def decorator(func):
    print(f"decorator:{locals()=}")
    def wrapper(*args, **kwargs):
        print(f"wrapper:{locals()=}")
        print(f"{func(*args, **kwargs)=}")
    return wrapper

# @test("тест")
def func1(text: str):
    return text

# @decorator
def func2(text: str):
    return text

# msg1("функция1 запущено")
# msg2("функция2 запущено")

print()
print(f"{func1=}")
test("Аргументы декоратор")(func1)("Аргументы функции1")

print()
print(f"{func2=}")
decorator(func2)("Аргументы функции2")