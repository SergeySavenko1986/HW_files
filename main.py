############################## Задача №1
from pprint import pprint

with open('file_1.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        cook_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for _ in range(ing_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'name': name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[cook_name] = ingredients

    a = (cook_book)

pprint(a, sort_dicts=False)
