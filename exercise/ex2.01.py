print("Котов дома")  
cats_at_home = int(input())  
    
print("Котов всего")  
total_cats = int(input())  
    
if cats_at_home == total_cats:  
    print("Все дома, можно закрывать дверь")  
    
elif cats_at_home < total_cats:  
    p = total_cats - cats_at_home  
    print(p, "не хватает, надо подождать")  
    
elif cats_at_home > total_cats:  
    l = cats_at_home - total_cats  
    if l > 1:  
        print("На", l, "больше, ищи лишних")  
    else:  
        print("На", l, "больше, ищи лишнего")