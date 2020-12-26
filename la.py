Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> print(list(range(10,20)))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> for x in range(0,5):
	print('hello %s' % x)

	
hello 0
hello 1
hello 2
hello 3
hello 4
>>> hugeharypants=['huge','hairy','pants']
>>> for i in hugeharypants:
	print(i)
	print(i)

	
huge
huge
hairy
hairy
pants
pants
>>> hugeharypants=['huge','hairy','pants']
>>> for i in hugeharypants:
	print(i)
	
SyntaxError: multiple statements found while compiling a single statement
>>> hugeharypants=['huge','hairy','pants']
>>> for i in hugeharypants:
	print(i)
	for j in hugeharypants:
		print(j)

		
huge
huge
hairy
pants
hairy
huge
hairy
pants
pants
huge
hairy
pants
>>> 
