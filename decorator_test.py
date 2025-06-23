from functools import wraps
from random import randint
from typing import Callable

print('--------Декоратор с аргументами------------------')

def bar():
    print(1)

def decorator(errors):
    errors: list
    def func_wrapper(func):
        func: Callable

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func()
            except Exception as e:
                print(type(e).__name__)

                for error in errors:
                    print(error)
                    print(e.__class__)
                    print(isinstance(e, error[0]))
                    if error[0] is e.__class__:
                        error[1]()
                        break


            return

        return wrapper

    return func_wrapper

@decorator([(KeyError, bar), (IndexError, lambda : print(2))])
def foo():
    if randint(1,2) == 1:
        raise KeyError("bar")
    else:
        raise IndexError

foo()