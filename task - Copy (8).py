# Təkrar elemetlərdən ibarət list yaradın, sonra bu listdən təkrarlanmayan list yaradın

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)