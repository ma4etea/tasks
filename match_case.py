
"""
🧩 Задача: Меню команд

Напиши функцию menu_command(cmd: str), которая принимает строку-команду и выполняет соответствующее действие:
Команда	Результат
"start"	Печатает: Запуск системы...
"stop"	Печатает: Остановка системы...
"restart"	Печатает: Перезапуск...
"status"	Печатает: Система работает нормально.
"exit"	Печатает: Выход из программы.
любое другое	Печатает: Неизвестная команда.
Используй конструкцию match-case."""

def menu_command(cmd: str):

    match cmd:
        case "start":
            print("Запуск системы...")
        case "stop":
            print("Остановка системы...")
        case "restart":
            print("Перезапуск...")
        case "status":
            print("Система работает нормально.")
        case "exit":
            print("Выход из программы.")
        case _:
            print("Неизвестная команда.")

menu_command("start")
menu_command("stop")
menu_command("restart")
menu_command("status")
menu_command("exit")
menu_command("sdfdsf")
