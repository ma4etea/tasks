from typing import List

def combination_sum3(k: int, n: int) -> List[List[int]]:
    # Результат
    res: List[List[int]] = []
    # Если нужно больше чисел, чем есть (1..9) — сразу пусто
    if k > 9:
        return res

    # Вспомогательная рекурсивная функция
    def backtrack(start: int, path: List[int], current_sum: int):
        # Если длина пути достигла k
        if len(path) == k:
            if current_sum == n:
                res.append(path.copy())
            return
        # Перебираем кандидатов от start до 9
        for num in range(start, 10):  # 1..9 включительно
            # Быстрая проверка: если текущая сумма уже превысит n — можно выйти
            if current_sum + num > n:
                # Так как nums возрастают, дальше тоже будут превышать
                break
            # Отсечение: минимальная возможная сумма для заполнения оставшихся мест
            remaining_needed = k - len(path) - 1  # после добавления num
            if remaining_needed > 0:
                # минимальная добавочная сумма = (num+1) + (num+2) + ... на remaining_needed элементов
                min_possible = (num + 1 + (num + remaining_needed)) * remaining_needed // 2
                # максимальная добавочная сумма = 9 + 8 + ... (remaining_needed элементов)
                max_possible = sum(range(9, 9 - remaining_needed, -1))
                # Если даже с минимальной суммой превысим n, или с максимальной не дотянем — отсечём
                if current_sum + num + min_possible > n:
                    break
                if current_sum + num + max_possible < n:
                    # этот num слишком маленький, попробовать следующий
                    continue
            # Выбираем num
            path.append(num)
            backtrack(num + 1, path, current_sum + num)
            path.pop()

    backtrack(1, [], 0)
    return res

print(combination_sum3(2, 33try))