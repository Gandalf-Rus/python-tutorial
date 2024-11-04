print("Текущий год")
now_year = int(input())

print("Текущий месяц")
now_month = int(input())

print("Текущий день")
now_day = int(input())

print("-----")

print("Год конца срока годности")
end_year = int(input())

print("Месяц конца срока годности")
end_month = int(input())

print("День конца срока годности")

end_day = int(input())
if now_year == end_year and now_month == end_month and now_day == end_day:
    print("Продукт ещё сегодня годен, можно есть")
elif now_year == end_year and now_month == end_month and now_day < end_day:
            print('Продукт годен, ешь спокойно')
elif now_year == end_year and now_month < end_month:
            print('Продукт годен, ешь спокойно')
elif now_year < end_year:
     print('Продукт годен, ешь спокойно')
else:
    print('Продукт испортился')