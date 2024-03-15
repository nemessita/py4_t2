# İnputdan gələn iki rəqəm aralığında yerləşən rəqəmlərin cüt və ya tək olduğunu
# (əlavə olaraq cüt rəqəmlərin sayını hesablayın) tapıın

num1 = int(input("birinci: "))
num2 = int(input("ikinci: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i, end=" ")
    
# (əlavə olaraq cüt rəqəmlərin sayını hesablayın) tapıın?????????????????????????