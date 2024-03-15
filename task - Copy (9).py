# 3 rəqəmdən  ibarət list yaradın və bu listin rəqəmlərindən yarana biləcək kombinasiyaları çap edin

list = [1, 2, 3]
for i in list:
    for j in list:
        for k in list:
            if i != j and j != k and i != k:
                print(i, j, k)