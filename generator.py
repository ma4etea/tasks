
from datetime import datetime, timedelta

def set_deadline(seconds):
    return datetime.now() + timedelta(seconds=seconds)

def payload1():
    next_run = set_deadline(1)
    while True:
        now = datetime.now()
        if now >= next_run:
            print("1", now.time())
            next_run = set_deadline(1)
        yield  # "отдаём управление" шедулеру

def payload2():
    next_run = set_deadline(3)
    while True:
        now = datetime.now()
        if now >= next_run:
            print("2", now.time())
            next_run = set_deadline(3)
        yield

def scheduler(*tasks):
    """Простейший кооперативный шедулер"""
    while True:
        for task in tasks:
            next(task)

# создаём генераторы
p1 = payload1()
p2 = payload2()

scheduler(p1, p2)


