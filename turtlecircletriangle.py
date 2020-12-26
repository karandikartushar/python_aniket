import turtle
t=turtle.Pen()
t.up()
t.forward(-100)
t.down()
t.forward(300)
t.left(120)
for x in range(1,4):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(120)
t.right(180)
for y in range(1,4):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(120)
