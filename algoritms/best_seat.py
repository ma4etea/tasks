def best_seat(row: list[int]) -> int | None:
    best_index = None
    greater_range = 0
    current_range = 0
    beg, end = False, False
    index = 0
    while index < len(row):
        if row[index] == 1:
            beg = True
            index += 1
        else:
            while index < len(row) and row[index] == 0:
                current_range += 1
                index += 1
            if index < len(row) and row[index] == 1:
                end = True
            current_range = int(current_range // (beg + end))
            beg, end = False, False
            if current_range > greater_range:
                best_index = index + 1 - current_range
                greater_range = current_range

    print(f"{best_index=}")
    return best_index

print(f"{(best_seat([0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) == 1)=}")
print(f"{(best_seat([1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == 17)=}")
print(f"{(best_seat([1, 0, 1]) == 2)=}")
print(f"{(best_seat([1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) == 4)=}")
print(f"{(best_seat([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) in [4, 5])=}")
print(f"{(best_seat([0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) in [5, 6])=}")
print(f"{(best_seat([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) == 1)=}")

# Тут уже нужно понять что лучше с одной стороны 3 или некого. Тут работает что некого лучше, чем 3
print(f"{(best_seat([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]) == 1)=}")
print(f"{(best_seat([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]) == 19)=}")
