from turtle import *
import time

a = int(input("red:  a     ")) * 50
print("      -     -")
b = int(input("      b     ")) * 50
print()
a2 = int(input("blue: c     ")) * 50
print("      -     -")
b2 = int(input("      d     ")) * 50


t = Turtle()
t.speed(0)


# START
t.goto(0, 0)
t.goto(0, 300)
t.goto(0, 0)
t.goto(300, 0)
t.goto(0, 0)


t.speed(5)
t.color("#ff0000")
t.goto(b, a)
t.goto(0, 0)
t.color("#0000ff")
t.goto(b2, a2)

time.sleep(3)
