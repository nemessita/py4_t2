# a = {'ad':['Fuad','Rovsen','Orxan']}
# Proqram Sorushur :
#     Secim Edin : (1) Elave et (2) Sil
   
#     Error Mesajlari :
#         Ad daxil etmediniz
#         Bu ad bazada yoxdur

a = {'ad':['Fuad','Rovsen','Orxan']}
enter = input("Secim Edin : (1) add_info (2) delete_info:  ")

if enter == "1":
    add_info = input("Daxil edin : ")
    a['ad'].append(add_info)

elif enter == "2":
    delete_info = input("Daxil edin : ")
    if delete_info in a['ad']:
        a['ad'].remove(delete_info)
    else:
        print("del")
else:
    print("error")

print(a)