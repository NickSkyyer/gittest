place1 = 'Изысканные гамбургеры от Джо'# - вегетарианская: нет, веганская (строгая вегетарианская): нет, безглютеновая: нет.
place2 = 'Центральная пиццерия'# - вегетарианская: да, веганская: нет, безглютеновая: да.
place3 = 'Кафе за углом'# - вегетарианская: да, веганская: да, безглютеновая: да.
place4 = 'Блюда от итальянской мамы'# - вегетарианская: да, веганская: нет, безглютеновая: нет.
place5 = 'Кухня шеф-повара'# - вегетарианская: да, веганская: да, безглютеновая: да.

isVegetarian = input('Будет ли на ужине вегетарианец? ') == 'да'
isVegan = input('Будет ли на ужине веганец? ') == 'да'
isGlutenFree = input('Будет ли на ужине приверженец безглютеновой диеты? ') == 'да'

print('Вот ваши варианты ресторанов:')

if not isVegetarian and not isVegan and not isGlutenFree:
    print(place1)
elif isVegetarian and not isVegan and isGlutenFree:
    print(place2)
elif isVegetarian and not isVegan and not isGlutenFree:
    print(place4)

print(place3)
print(place5)
