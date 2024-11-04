print('Какая монета у Чебурашки (в копейках)')

moneys = int(input())

if  moneys < 100:
    print('мало')
elif moneys >= 100 and moneys < 500:
    print('не мало')
elif moneys >= 500:
    print('Много, сдачу давай!')