monster1 = int(input())
monster2 = int(input())
monster3 = int(input())
list1 = [monster1, monster2, monster3] # 4 -1 7
min_int = list1[0] # 4


for i in list1:
    if abs(min_int) > abs(i):
        min_int = i
    elif min_int == i:
        continue
    if min_int > 0:
        print("Right")
    if min_int < 0:
        print("Left")
