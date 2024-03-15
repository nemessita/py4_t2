# List yaradın , listin hər hansı dəyərinin indeksini tapın və həmin indeksə başqa dəyər əlavə edin


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
enter = input("Secim Edin : (1) indexini_yoxla (2) hemen_indexe_deyer_ver:  ")
if enter == "1":
    enter1 = int(input("Daxil edin : "))
    index = list.index(enter1)
    print(index)
elif enter == "2":
    enter2 = int(input("Daxil edin index : "))
    list[enter2] = int(input("Daxil edin deyer : "))
    print(list)
else:
    print("error")







# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# enter1 = int(input("Daxil edin : "))
# index = list.index(enter1)
# print(index)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# enter2 = int(input("Daxil edin index : "))
# list.__add__([enter2])

# print(list)


