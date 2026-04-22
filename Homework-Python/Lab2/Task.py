#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product

# =========================
# ЗАДАНИЕ 1
# =========================
def task1():
    return len(list(product(['X', 'Y', 'Z'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'])))


# =========================
# ЗАДАНИЕ 2
# =========================
def to_base3(n):
    result = ''
    while n:
        result = str(n % 3) + result
        n //= 3
    return result


def task2():
    return to_base3(9**8 + 3**5 - 9).count('2')


# =========================
# ЗАДАНИЕ 3
# =========================
def task3():
    result = []

    for n in range(40000, 50001):
        odd_divs = set()

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i % 2:
                    odd_divs.add(i)
                if (n // i) % 2:
                    odd_divs.add(n // i)

        if len(odd_divs) == 5:
            result.append(n)

    return result


# =========================
# ВЫВОД
# =========================
if __name__ == "__main__":
    print("Задание 1:", task1())
    print("Задание 2:", task2())
    print("Задание 3:", task3())