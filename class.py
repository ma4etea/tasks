
"""🔧 Задача: Менеджер задач

Реализуй класс Task, представляющий задачу, и класс TaskManager, управляющий списком задач.
Класс Task:

    Имеет поля:

        title — название задачи (строка)

        completed — выполнена ли задача (bool, по умолчанию False)

    Метод mark_done() — отмечает задачу как выполненную

Класс TaskManager:

    Хранит список задач

    Методы:

        add_task(title: str) — добавляет новую задачу

        complete_task(title: str) — отмечает задачу с таким названием как выполненную

        get_pending_tasks() — возвращает список названий невыполненных задач

        get_completed_tasks() — возвращает список названий выполненных задач

    manager = TaskManager()
    manager.add_task("Купить хлеб")
    manager.add_task("Позвонить врачу")
    manager.complete_task("Купить хлеб")

    print(manager.get_pending_tasks())    # ['Позвонить врачу']
    print(manager.get_completed_tasks())  # ['Купить хлеб']

    """


class Task:
    def __init__(self, title: str):
        self.title: str = title
        self.completed: bool = False


class TaskManager:

    def __init__(self):
        self.tasks: list[Task] = []
        # self.complete_tasks: list[Task] = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, title):
      for task in self.tasks:
          if task.title == title and task.completed == False:
              task.completed = True
              return print(f"{title}: задача завершена")

    def get_pending_tasks(self):
        return [task.title for task in self.tasks if task.completed == False]

    def get_completed_tasks(self):
        return [task.title for task in self.tasks if task.completed == True]

manager = TaskManager()
manager.add_task("Купить хлеб")
manager.add_task("Позвонить врачу")
manager.complete_task("Купить хлеб")

print(manager.get_pending_tasks())  # ['Позвонить врачу']
print(manager.get_completed_tasks())  # ['Купить хлеб']