#virtual printer
# Daxil Edin : Java
# Say: 6

# 1 Java
# 2 Java
# 3 Java
# 4 Java
# 5 Java
# 6 Java

add_enter = input("Daxil edin : ")
add_number = int(input("Say: "))

if add_number > 0:
    i = 1
    while i <= add_number:
        print(i, add_enter)
        i += 1
else:
    print("Error")


