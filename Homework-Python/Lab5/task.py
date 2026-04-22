#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =========================
# ГЕНЕРАТОР ЧТЕНИЯ ФАЙЛА
# =========================
def read_file_with_limit(filename, max_length):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # если строка длиннее лимита — обрезаем
            if len(line) > max_length:
                yield line[:max_length]
            else:
                yield line


# =========================
# ФУНКЦИЯ ПЕРЕВОРОТА СЛОВ
# =========================
def reverse_words(line):
    words = line.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# =========================
# ОСНОВНАЯ ЗАДАЧА
# =========================
def process_file(filename, max_length):
    gen = read_file_with_limit(filename, max_length)

    # применяем map
    result = map(reverse_words, gen)

    return list(result)


# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    filename = "input.txt"
    max_length = 20

    result = process_file(filename, max_length)

    print("Результат:")
    for line in result:
        print(line)