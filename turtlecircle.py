def make_triangle(length,t):
    t.circle(length)
import turtle
t=turtle.Pen()
for i in range(1,11):
    make_triangle(9*i,t)
    t.up()
    t.left(99)
    t.forward(-9)
    t.right(98)
    t.down()
t.hide()
