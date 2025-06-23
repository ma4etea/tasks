

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0


    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print('👉 Недостаточно средств')

    def display_balance(self):
        print(f'👉 Баланс: {self.balance}')

    def __str__(self):
        return f"💳 Счёт {self.owner}, баланс: {self.balance} ₽"




account = BankAccount("Александр")
account.deposit(1000)
account.withdraw(500)
account.display_balance()  # 👉 Баланс: 500

account.withdraw(700)     # 👉 Недостаточно средств

print(account)



#----------------------------------------------------------------------------------


class User:

    total_users = 0
    all_users = []

    def __init__(self, name):
        self.name = name
        User.total_users += 1
        User.all_users.append(name)



    @classmethod
    def show_stats(cls):
        print(f'👉 Всего пользователей: {cls.total_users}')
        print(f'👉 Имена: {cls.all_users}')

    @staticmethod
    def greet():
        print(f'👉 Добро пожаловать!')

u1 = User("Анна")
u2 = User("Борис")

User.show_stats()
# 👉 Всего пользователей: 2
# 👉 Имена: ['Анна', 'Борис']

User.greet()
# 👉 Добро пожаловать!


#----------------------------------------------------------------------------------

class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self._price = 0
        self._discount = 0
        self.price = price  # это уже сетер
        self.discount = discount # это уже сетер

    @property
    def price_with_discount(self):
        return self._price - self._price*self._discount/100

    @property
    def price(self):
        return self._discount

    @price.setter
    def price(self, amount):
        if 0 < amount:
            self._price = amount
        else:
            print('👉 ❌ Цена должна быть положительной')

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, amount):
        if 0 <= amount <= 100:
            self._discount = amount
        else:
            print('👉 ❌ Неверное значение скидки')


p = Product("Молоко", 100, 10)

print(p.price_with_discount)  # 👉 90.0

p.discount = 50
print(p.price_with_discount)  # 👉 50.0

p.discount = 150              # 👉 ❌ Неверное значение скидки
p.price = -20                 # 👉 ❌ Цена должна быть положительной




#----------------------------------------------------------------------------------

class Employee:
    def __init__(self, name, base_salary, tax_rate):
        self.name = name
        self._base_salary = 0
        self._tax_rate = 0

        self.base_salary = base_salary
        self.tax_rate = tax_rate

    @property
    def salary_after_tax(self):
        return self._base_salary - self._base_salary*self._tax_rate/100

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if 0 < value:
            self._base_salary = value
        else:
            print('👉 ❌ Зарплата должна быть положительной')

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        if 0 <= value <= 100:
            self._tax_rate = value
        else:
            print('👉 ❌ Недопустимая ставка налога')



e = Employee("Иван", 50000, 13)

print(e.salary_after_tax)  # 👉 43500.0

e.tax_rate = 105           # 👉 ❌ Недопустимая ставка налога
e.base_salary = -10000     # 👉 ❌ Зарплата должна быть положительной


print('----------------------------------------------------------------------------------')
print('__repr__')



class Colors:
    def __init__(self, color, num):
        self.color = color
        self.num = num

    def __repr__(self):
        return f'Цвет {self.color}, номер {self.num}'

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num > other.num



red=Colors(color='красный', num=3)
blue=Colors(color='синий', num=2)
green=Colors(color='зеленый', num=1)

print(red)
print(blue)
print(green)
print(sorted([red,blue,green]))

print('----------------------------------------------------------------------------------')
print('cls')

class Songs:
    def __init__(self, _song):
        self.song = _song

    @classmethod
    def default_song(cls):
        return cls(_song='Стинг')

song = Songs.default_song()

print(song.song)


print('----------------------------------------------------------------------------------')



class Call1:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(self.name)
        print(args)
        print(kwargs)

a = Call1('Alexander')

a(1,2,3, a=1,b=2,c=3)