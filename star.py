import turtle
def make_star(size,points):
    angle1=0
    angle2=0
    if points==4:
        angle1=170
        angle2=280
    elif points==5:
        angle1=100
        angle2=185
    elif points==6:
        angle1=145
        angle2=275
    elif points==7:
        angle1=167
        angle2=244.5
    elif points==8:
        angle1=165
        angle2=240
    elif points==9:
        angle1=175
        angle2=225
    elif points==10:
        angle1=168
        angle2=228
    else:
        print('sorry.Program over.')
    t.color(1,1,0)
    t.begin_fill()
    for x in range(1,((points*2)+1)):  
        t.forward(size)
        if x%2==0:
            t.left(angle1)
        else:
            t.left(angle2)
    t.end_fill()
t=turtle.Pen()
a=int(input('Enter the size:'))
b=int(input('Enter the number of points from 4 to 10:'))
make_star(a,b)
            






