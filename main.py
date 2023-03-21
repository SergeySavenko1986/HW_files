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
print('\n')

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in a:
            for ingr in a[dish]:
                ingr['quantity'] = int(quantity) * person_count
                final_dict = ingr.pop('name') #просто удаляем из словаря имя каждого ингредиента
                result[final_dict] = ingr
    return result

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5))