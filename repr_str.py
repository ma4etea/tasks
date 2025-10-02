class MyClass:
    def __str__(self):
        return "Описание для человека - Класс MyClass"

    def __repr__(self):
        return "Описание для разраба - MyClass"

obj = MyClass()

print(obj.__str__())
print(obj.__repr__())