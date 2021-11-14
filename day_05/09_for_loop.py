Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_04/08_if_else.py =====
Enter the first number: 23
Enter the second number: 34
--------------------------------------------------
The number is negative
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_04/08_if_else.py =====
Enter the first number: 12
Enter the second number: 2
--------------------------------------------------
The number is positive
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_04/08_if_else.py =====
Enter the first number: 3
Enter the second number: 3
--------------------------------------------------
The number is zero
>>> 
>>> 
>>> # ------------------ Looping
>>> 
>>> 
>>> for c in "python":
	print(c)

	
p
y
t
h
o
n
>>> for c in "python":
	print(c.upper(), end=' ')

	
P Y T H O N 
>>> 
>>> for item in ["red", "green", "blue"]:
	print(item.capitalized())

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(item.capitalized())
AttributeError: 'str' object has no attribute 'capitalized'
>>> for item in ["red", "green", "blue"]:
	print(item.capitalize())

	
Red
Green
Blue
>>> D = {'name':'Sunil', 'age':35, 'company':'Oracle', 'country':'UK'}
>>> for item in D:
	print(item)

	
name
age
company
country
>>> for item in D.keys():
	print(item)
	\

	  
SyntaxError: invalid syntax
>>> for item in D.keys():
	print(item)

	
name
age
company
country
>>> for item in D.values():
	print(item)

	
Sunil
35
Oracle
UK
>>> for item in D.items():
	print(item)

	
('name', 'Sunil')
('age', 35)
('company', 'Oracle')
('country', 'UK')
>>> 
>>> 
>>> 
>>> c = ("red", "green", "blue")
>>> r, g, b = c
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> 
>>> 
>>> r,g = c
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    r,g = c
ValueError: too many values to unpack (expected 2)
>>> r, g, *x = c
>>> r
'red'
>>> g
'green'
>>> x
['blue']
>>> 
>>> 
>>> for key, value in D.items():
	print(key, ' -----> ', value)

	
name  ----->  Sunil
age  ----->  35
company  ----->  Oracle
country  ----->  UK
>>> 
>>> 

>>> # ------------------- Example
>>> 
>>> # Multiplication table
>>> print(5, ' X ', 1, ' = ', (5*1))
5  X  1  =  5
>>> for n in [1, 2, 3, 4]:
	print(5, ' X ', n, ' = ', (5*n))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 20, 2))
[10, 12, 14, 16, 18]
>>> list(range(20 ,10, 2))
[]
>>> list(range(20 ,10))
[]
>>> list(range(20 ,10. -1))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(range(20 ,10. -1))
TypeError: 'float' object cannot be interpreted as an integer
>>> list(range(20 ,10, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> 
>>> for n in range(1, 11):
	print(5, ' X ', n, ' = ', (5*n))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> 
>>> # ------------------- Loop controls
>>> for n in range(1, 11):
	print(5, ' X ', n, ' = ', (5*n))
	if(n == 7):
		break

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
>>> 
>>> 
>>> for n in range(1, 11):
	if(n == 7):
		continue
	print(5, ' X ', n, ' = ', (5*n))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # ----------------------- while
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  55  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X  1  =  5
5  X Traceback (most recent call last):
  File "<pyshell#94>", line 2, in <module>
    print(5, ' X ', i, ' = ', (5*i))
KeyboardInterrupt
>>> while i <= 10:
	print(5, ' X ', i, ' = ', (5*i))
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
