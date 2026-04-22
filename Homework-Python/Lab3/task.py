#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# =========================
# ЗАДАНИЕ 1
# =========================

# Без рекурсии
def sum_nested_iterative(lst):
    total = 0
    stack = list(lst)

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            total += item

    return total


# С рекурсией
def sum_nested_recursive(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested_recursive(item)
        else:
            total += item
    return total


# =========================
# ЗАДАНИЕ 2
# =========================

# Без рекурсии
def calc_iterative(n):
    a, b = 1, 1

    for _ in range(2, n + 1):
        new_a = 0.5 * (math.sqrt(b) + math.sqrt(a))
        new_b = 1.5 * math.sqrt(b) + 0.5 * (a ** 2)
        a, b = new_a, new_b

    return a, b


# С рекурсией
def calc_recursive(n):
    if n == 1:
        return 1, 1

    a_prev, b_prev = calc_recursive(n - 1)

    a = 0.5 * (math.sqrt(b_prev) + math.sqrt(a_prev))
    b = 1.5 * math.sqrt(b_prev) + 0.5 * (a_prev ** 2)

    return a, b


# =========================
# ЗАПУСК
# =========================

if __name__ == "__main__":
    test_list = [1, [2, [3, 4, [5]]]]

    print("Сумма (без рекурсии):", sum_nested_iterative(test_list))
    print("Сумма (рекурсия):", sum_nested_recursive(test_list))

    n = 5

    a1, b1 = calc_iterative(n)
    a2, b2 = calc_recursive(n)

    print("\nПоследовательность (без рекурсии):", round(a1, 3), round(b1, 3))
    print("Последовательность (рекурсия):", round(a2, 3), round(b2, 3))