from typing import Generator


def read_file_by_words(file_name: str) -> Generator[str | list[str], int | None, None]:
    result = []
    num = None

    with open(file_name, encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                if num is None:
                    num = yield word
                else:
                    # print("result.append(word)")
                    result.append(word)
                    # print("после result.append(word)")
                    num -= 1

                    if num == 0:
                        num = yield result
                        result = []

                if num == 0:
                    raise ValueError

        if result:
            yield result

# Файл содержит только одно слово
rfbw = read_file_by_words("file1.txt") # текст в файле "Когда word2"
print(next(rfbw))     # Когда
print(rfbw.send(-1))
print(rfbw.send(2))   # ['word2']
try:
    next(rfbw)     # StopIteration
except StopIteration:
    print("StopIteration")
print()

rfbw = read_file_by_words("file.txt")

print(next(rfbw))     # Когда
print(rfbw.send(3))   # ['старый', 'легаси', 'код']
print(next(rfbw)   )  # встречается
print(rfbw.send(5) )  # ['с', 'новым', 'рефакторингом', 'в', 'production']
print(list(rfbw)  )   # ['случается', 'магия', 'Или', 'баги']

# Попытка чтения из пустого файла
try:
    next(rfbw)     # StopIteration
except StopIteration:
    print("StopIteration")



