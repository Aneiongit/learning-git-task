# Task : 
# Zadanie 1
# Pamiętasz zadanie z listą zakupów?
# Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni,
# w której kupujemy chleb, bułki oraz pączka. Poza tym po drodze wstąpimy też do warzywniaka,
# gdzie kupimy marchew, seler i rukolę.
# W pliku, który właśnie utworzyliśmy:
# zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, 
# a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
# Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: 
# Idę do <sklep> i kupuję tam <rzeczy>.
# Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów 
# i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć 
# taką funkcjonalność).
# Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna 
# liczba towarów, które są na listach.

# declaring shops and items to buy
shopping = {'piekarnia': ['chleb', 'pączek', 'bułki'],
            'warzywniak': ['marchew', 'seler', 'rukola']
            }

# capitalizing shops names
bakery = (list(shopping.keys())[0]).capitalize()
vege = (list(shopping.keys())[1]).capitalize()

# counting the number of items to buy
num_of_items = sum(map(len, shopping.values()))

# capitalizing items to buy
bakery_items_cap = [i.title() for i in shopping.get('piekarnia')]
vege_items_cap = [i.title() for i in shopping.get('warzywniak')]

# printing results
print('Lista zakupów:')
print('Idę do', bakery + ', kupuję tu następujące rzeczy:', str(bakery_items_cap) + '.')
print('Idę do', vege + ', kupuję tu następujące rzeczy:', str(vege_items_cap) + '.')
print('W sumie kupuję', num_of_items, 'produktów.')
