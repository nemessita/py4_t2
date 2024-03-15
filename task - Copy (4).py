# Listin içində bir neçə list olsun, 3ci elementinin 2ci indeksinə dəyər əlavə edin

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

main_list = [list1, list2, list3]

list_index = int(input("Secim Edin : (0,1,2) index:  "))
element_index = int(input("element_index : "))
new_value = input("new_value : ")

main_list[list_index][element_index] = new_value
new_list = main_list[list_index]

print(new_list)



# main_list[list3][2] = input("Secim Edin : index:  ")
# new_list = []

# print(new_list)
