from turtle import *
def draw_square(a,b):
    for i in range(4):
        color(a)
        forward(b)
        left(90)

draw_square("red",200)

mainloop()

