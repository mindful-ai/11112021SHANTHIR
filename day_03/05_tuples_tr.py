Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ("red", "green", "blue")
>>> T[0]
'red'
>>> T[0] = "orange"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    T[0] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # -------------- Adding and removing elements directly is not allowed
>>> 
>>> #--------------- Re-arranging elements
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
>>> reversed(T)
<reversed object at 0x000001EF6FF99EB8>
>>> list(reversed(T))
['blue', 'green', 'red']
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> 
>>> # ------------------------- searching
>>> 
>>> T
('red', 'green', 'blue')
>>> 'red' in T
True
>>> T.count('red')
1
>>> T.index('red')
0
>>> 
>>> # --------------------------- iterating
>>> 
>>> for item in T:
	print(T)

	
('red', 'green', 'blue')
('red', 'green', 'blue')
('red', 'green', 'blue')
>>> for item in T:
	print(item)

	
red
green
blue
>>> 
>>> # -------------------------- How to do mdifications
>>> 
>>> T
('red', 'green', 'blue')
>>> 
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L[1] = "orange"
>>> L
['red', 'orange', 'blue']
>>> T = tuple(L)
>>> T
('red', 'orange', 'blue')
>>> 
>>> # ---------------------- operators for both lists and tuples
>>> 
>>> T1 = ("red", "green", "blue")
>>> T2 = ("black", "white", "grey")
>>> 
>>> T1 + T2
('red', 'green', 'blue', 'black', 'white', 'grey')
>>> T1
('red', 'green', 'blue')
>>> T2
('black', 'white', 'grey')
>>> T3 = T1 + T2
\
>>> T3
('red', 'green', 'blue', 'black', 'white', 'grey')
>>> 
>>> 
>>> T1 * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> 
>>> 
>>> len(T1 + T2)
6
>>> 
>>> type(L1) is str
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    type(L1) is str
NameError: name 'L1' is not defined
>>> type(T1) is str
False
>>> type(T1) is tuple
True
>>> 
>>> 'red' in T1 + T2
True
>>> 
>>> T1
('red', 'green', 'blue')
>>> del T1[1]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    del T1[1]
TypeError: 'tuple' object doesn't support item deletion
>>> L
['red', 'orange', 'blue']
>>> del L[1]
>>> L
['red', 'blue']
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
