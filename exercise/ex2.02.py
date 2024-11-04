print('Сколькo у белки орехов')

nuts = int(input())

print('Сколько подруг зовет белка ')

friends = int(input())

if nuts == 0:
    print('Гостей звать не надо: орехов нет')
elif nuts < friends:
    print('Гостей звать не надо: белка съест всё сама')
elif nuts == friends:
    print('Гостей звать не надо: белке не хватит орехов')
else:
    print('Гостей зовем: Каждой подруге достанется ', nuts // friends, ' ореха,белке останется ', nuts % friends, ' ореха/ов')