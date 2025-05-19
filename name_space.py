"""Это докстринг модуля"""

a = 'глобальная'


class Go:
    """Это докстринг класса Go"""

def go():
    """Это докстринг функции go"""
    b = 'локальная'
    print(globals())
    print(locals())

    print(Go.__doc__)


go()