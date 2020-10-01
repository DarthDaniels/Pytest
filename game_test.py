monster1, act1 = int(input()), True
monster2, act2 = int(input()), True
monster3, act3 = int(input()), True
min_int = monster1

for count in range(3):
    if abs(min_int) > abs(monster1) and act1:
        min_int = monster1
        act1 = False
    if abs(min_int) > abs(monster2) and act2:
        min_int = monster2
        act2 = False
    if abs(min_int) > abs(monster3) and act3:
        min_int = monster3
        act3 = False
    if min_int > 0:
        print("Right")
    if min_int < 0:
        print("Left")
