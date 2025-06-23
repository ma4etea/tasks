import threading
import time
from datetime import datetime
from functools import wraps
from itertools import count
from random import randint
from typing import Callable


def log_call(func):
    name = func.__name__

    @wraps(func)  # переносит оригинальные метаданные
    def wrapper(*args, **kwargs):
        print(f'🔔 Вызов: {name}')
        result = func(*args, **kwargs)
        print(f'✅ Завершено: {name}')
        return result

    return wrapper


@log_call
def greet(name):
    print(f"Привет, {name}!")


greet("Аня")

print(greet.__name__)  # greet

# _____________________________________________________
print('-------------------------------------------------------')


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"🕒 Время выполнения {func.__name__}: {(end - start).total_seconds()} сек")
        return result

    return wrapper


@measure_time
def slow_add(a, b):
    time.sleep(0.5)
    return a + b


slow_add(1, 2)

# _____________________________________________________
print('-------------------------------------------------------')


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count1 = 0
            result = None
            while count1 < n:
                count1 = count1 + 1
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Привет, {name}!")
    return f"Hello {name}"


greet("Аня")

# _____________________________________________________
print('-------------------------------------------------------')

current_user = {"name": "Аня", "role": "admin"}


def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user['role'] == role:
                result = func(*args, **kwargs)
                return result
            else:
                print('❌ Доступ запрещён: требуется роль admin')

        return wrapper

    return decorator


@require_role("admin")
def delete_all():
    print("🔥 Все данные удалены!")


delete_all()

# _____________________________________________________
print('-------------------------------------------------------')


def cache(func):
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  # тут магия для хэша
        if key in cache_dict:  # тут фактически проверка хэша

            print('⚡ Возвращено из кэша')
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


@cache
def slow_square(x):
    print(f"Вычисляем квадрат {x}")
    time.sleep(1)  # имитируем долгую работу
    return x * x


print(slow_square(3))  # вычисляет и кеширует
print(slow_square(3))  # берёт из кеша

# _____________________________________________________
print('-------------------------------------------------------')

counter = {"failures": 0}


def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count1 = 0
            result = None
            for attempt in range(n):
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError:
                    if attempt == n - 1:
                        raise  # пробрасываем последний раз

            return result

        return wrapper

    return decorator


@retry(3)
def flaky():
    if counter["failures"] < 2:
        counter["failures"] += 1
        raise ValueError("Падаем специально")
    return "🎉 Успех!"


print(flaky())

# _____________________________________________________
print('-------------------------------------------------------')


import threading
import time
from functools import wraps

def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result_container = {}
            exception_container = {}

            def target():
                try:
                    result_container["result"] = func(*args, **kwargs)
                except Exception as e:
                    exception_container["error"] = e

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(seconds)

            if thread.is_alive():
                raise TimeoutError(f"Функция превысила лимит в {seconds} секунд")
            if "error" in exception_container:
                raise exception_container["error"]

            return result_container.get("result")

        return wrapper
    return decorator



@timeout(2)
def slow():
    time.sleep(3)
    return "Не дождались..."

@timeout(2)
def fast():
    time.sleep(1)
    return "Успели!"

print(fast())    # ✅ Успели!
# print(slow())    # ❌ TimeoutError


# _____________________________________________________
print('-------------------------------------------------------')

request_token = "admin_secret"

def require_auth(token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if token and token == request_token:
                return func(*args, **kwargs)
            else:
                print('🚫 Неверный токен доступа')

        return wrapper

    return decorator




@require_auth("admin_secret")
def delete_user():
    print("🗑 Пользователь удалён")

delete_user()


# _____________________________________________________
print('-------------------------------------------------------')


request_token = "admin"

def log_call(func):
    name = func.__name__

    @wraps(func)  # переносит оригинальные метаданные
    def wrapper(*args, **kwargs):
        print(f'🔔 Вызов: {name}')
        result = func(*args, **kwargs)
        print(f'✅ Завершено: {name}')
        return result

    return wrapper

def require_auth(token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if token and token == request_token:
                return func(*args, **kwargs)
            else:
                print('🚫 Неверный токен доступа')

        return wrapper

    return decorator

@log_call
@require_auth("admin")
def delete_user():
    print("🗑 Пользователь удалён")

delete_user()

print('--------Декоратор без аргументов------------------')


class LogCall:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'🔔 Вызов: {self.func.__name__}')
        result = self.func(*args, **kwargs)
        print(f'✅ Завершено: {self.func.__name__}')
        return result


log = LogCall

@log
def greet(name):
    print(f"Привет, {name}!")

greet("Аня")

print('--------Декоратор с аргументами------------------')

class LogCall:
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{self.level}] 🔔 Вызов: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{self.level}] ✅ Завершено: {func.__name__}")
            return result
        return wrapper


log = LogCall

@log('INFO')
def greet(name):
    print(f"Привет, {name}!")

greet("Аня")


print('--------Декоратор с аргументами------------------')

def bar():
    print(1)

def decorator(errors):
    errors: list
    def func_wrapper(func):
        func: Callable

        @wraps(func)
        def wrapper(*args, **kwargs):
            for error in errors:
                try:
                    func()
                except error[0]:
                    error[1]()

            return

        return wrapper

    return func_wrapper

@decorator([(KeyError, bar), (IndexError, lambda _: print(2))])
def foo():
    if randint(1,2) == 1:
        raise KeyError("bar")
    else:
        raise IndexError
