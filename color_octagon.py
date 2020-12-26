import turtle
t=turtle.Pen()
t.color(1,1,0)
t.begin_fill()
for x in range(1,9):
    t.forward(50)
    t.right(45)
t.end_fill()
t.color(0,0,0)
for x in range(1,9):
    t.forward(50)
    t.right(45)
t.hideturtle()
