Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> import random
>>> tk=Tk()
>>> canvas=Canvas(width=400,heigt=400)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    canvas=Canvas(width=400,heigt=400)
  File "C:\Users\Rashmi\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2399, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "C:\Users\Rashmi\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2293, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: unknown option "-heigt"
>>> canvas=Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> def random_rectangle(width,height):
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1+random.randrange(width)
	y2=y1+random.randrange(height)
random_rectangle=(400,400)
SyntaxError: invalid syntax
>>> random_rectangle=(400,400)
>>> for x in range(0,100):
	random_rectangle(400,400)
	
