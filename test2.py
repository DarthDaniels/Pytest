position = int(input())
finish = int(input())
wall_1 = int(input())
wall_2 = int(input())

for i in range(position, finish):
    if i + 1 == wall_1 or i + 1 == wall_2:
        print("Прыжок")
        i += 1
        continue
    else:
        print("Шаг")
