#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Лампа (уже есть, но оставим красиво)
lamp_items = store[goods['Лампа']]
lamp_quantity = lamp_items[0]['quantity']
lamp_cost = lamp_items[0]['quantity'] * lamp_items[0]['price']
print('Лампа -', lamp_quantity, 'шт, стоимость', lamp_cost, 'руб')

# Стол
table_items = store[goods['Стол']]
table_quantity = table_items[0]['quantity'] + table_items[1]['quantity']
table_cost = (
    table_items[0]['quantity'] * table_items[0]['price'] +
    table_items[1]['quantity'] * table_items[1]['price']
)
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

# Диван
sofa_items = store[goods['Диван']]
sofa_quantity = sofa_items[0]['quantity'] + sofa_items[1]['quantity']
sofa_cost = (
    sofa_items[0]['quantity'] * sofa_items[0]['price'] +
    sofa_items[1]['quantity'] * sofa_items[1]['price']
)
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

# Стул
chair_items = store[goods['Стул']]
chair_quantity = (
    chair_items[0]['quantity'] +
    chair_items[1]['quantity'] +
    chair_items[2]['quantity']
)
chair_cost = (
    chair_items[0]['quantity'] * chair_items[0]['price'] +
    chair_items[1]['quantity'] * chair_items[1]['price'] +
    chair_items[2]['quantity'] * chair_items[2]['price']
)
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')