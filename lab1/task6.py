#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# вставляем медведя между львом и кенгуру (индекс 1)
zoo.insert(1, 'bear')
print(zoo)

# добавляем птиц в конец списка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# убираем слона
zoo.remove('elephant')
print(zoo)

# выводим номера клеток (для людей — с 1, а не с 0)
lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1

print('Лев сидит в клетке №', lion_index)
print('Жаворонок сидит в клетке №', lark_index)
