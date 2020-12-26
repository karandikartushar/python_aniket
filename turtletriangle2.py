def make_triangle(length,t):
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
import turtle
t=turtle.Pen()
for i in range(1,21):
    make_triangle(12.5*i,t)
    t.up()
    t.forward(4)
    t.left(120)
    t.forward(-4)
    t.down()
    
