shopping = {'piekarnia': ['chleb', 'pączek', 'bułki'],
            'warzywniak': ['marchew', 'seler', 'rukola']
            }

bakery = (list(shopping.keys())[0]).capitalize()
vege = (list(shopping.keys())[1]).capitalize()
num_of_items = sum(map(len, shopping.values()))
bakery_items_cap = [i.title() for i in shopping.get('piekarnia')]
vege_items_cap = [i.title() for i in shopping.get('warzywniak')]

print('Lista zakupów')
print('Idę do', bakery + ', kupuję tu następujące rzeczy:', str(bakery_items_cap) + '.')
print('Idę do', vege + ', kupuję tu następujące rzeczy:', str(vege_items_cap) + '.')
print('W sumie kupuję', num_of_items, 'produktów.')