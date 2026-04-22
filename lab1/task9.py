#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создаём множества
garden_set = set(garden)
meadow_set = set(meadow)

# все виды цветов
print(garden_set | meadow_set)

# растут и там и там
print(garden_set & meadow_set)

# только в саду
print(garden_set - meadow_set)

# только на лугу
print(meadow_set - garden_set)