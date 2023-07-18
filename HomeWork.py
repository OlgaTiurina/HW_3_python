import re
from collections import Counter

# В большой текстовой строке подсчитать количество встречаемых слов и 
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = input('Введите текст: ')
print(top_10_words(text))

# --------------------------------------------------------------------------
# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = []
lstNum = int(input('Введите нужное колличество значений в список: '))
num = 1
for _ in range(lstNum):
    lst.append(int(input(f'Введите {num} число: ')))
    num += 1
print(f'Ваш лист:\n{lst}')

print(find_duplicates(lst))

# -------------------------------------------------------------------------
# Создайте словарь со списком вещей для похода в качестве ключа и их массой 
# в качестве значения. Определите какие вещи влезут в 
# рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight))