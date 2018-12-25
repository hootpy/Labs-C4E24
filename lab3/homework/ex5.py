from turtle import *

def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        right(144)
        forward(length)

draw_star(100,200,300)
mainloop()