Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> L = ["red", "green", "blue", 1, 2.4, -5.6, [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> # ------------------- subscripting/ accessing values
>>> L[0]
'red'
>>> L[2]
'blue'
>>> L[-1]
[1, 2, 3]
>>> L[-1][1]
2
>>> L[2:5]
['blue', 1, 2.4]
>>> L[:5]
['red', 'green', 'blue', 1, 2.4]
>>> L[2:]
['blue', 1, 2.4, -5.6, [1, 2, 3]]
>>> L[::2]
['red', 'blue', 2.4, [1, 2, 3]]
>>> L[::-1]
[[1, 2, 3], -5.6, 2.4, 1, 'blue', 'green', 'red']
>>> 
>>> # ------------------------- mutablity
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> L[2]
'blue'
>>> L[2][2]
'u'
>>> L[2]
'blue'
>>> type(L[2])
<class 'str'>
>>> L[2][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L[2][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # Lists are mutable, but the elements in the list need not be mutable
>>> 
>>> # -------------------------- Adding elemtns
>>> 
>>> L
['red', 'yellow', 'blue']
>>> L.append("green")
>>> L
['red', 'yellow', 'blue', 'green']
>>> L.append("golden")
>>> L
['red', 'yellow', 'blue', 'green', 'golden']
>>> L.insert(1, "orange")
>>> L
['red', 'orange', 'yellow', 'blue', 'green', 'golden']
>>> 
>>> L1 = ["black", "white"]
>>> 
>>> L.extend(L1)
>>> L
['red', 'orange', 'yellow', 'blue', 'green', 'golden', 'black', 'white']
>>> L1
['black', 'white']
>>> L
['red', 'orange', 'yellow', 'blue', 'green', 'golden', 'black', 'white']

>>> L = ['red', 'yellow', 'blue']
>>> L[1]
'yellow'
>>> L[1] = L1
>>> L
['red', ['black', 'white'], 'blue']
>>> 
>>> 
>>> L = ['red', 'yellow', 'blue']
>>> L[1:2]
['yellow']
>>> L[1:2] = L1
>>> L
['red', 'black', 'white', 'blue']
>>> 
>>> 
>>> # ----------------------------- Removing elements
>>> 
>>> L
['red', 'black', 'white', 'blue']
>>> L.pop()
'blue'
>>> L
['red', 'black', 'white']
>>> L.pop(2)
'white'
>>> L
['red', 'black']
>>> L.remove("red")
>>> L
['black']
>>> 
>>> # ----------------------------- search for elements
>>> 
>>> L = ['red', 'black', 'white', 'blue']
>>> L.index("black")
1
>>> "white" in L
True
>>> L.append("red")
>>> L
['red', 'black', 'white', 'blue', 'red']
>>> L.count("red")
2
>>> 
>>> # --------------------------- re-arranging elements
>>> 
>>> L
['red', 'black', 'white', 'blue', 'red']
>>> sorted(L)
['black', 'blue', 'red', 'red', 'white']
>>> reversed(L)
<list_reverseiterator object at 0x000001406FD2C9B0>
>>> list(reversed(L))
['red', 'blue', 'white', 'black', 'red']
>>> L
['red', 'black', 'white', 'blue', 'red']
>>> 
>>> 
>>> 
>>> L.sort()
>>> L
['black', 'blue', 'red', 'red', 'white']
>>> L.reverse()
>>> L
['white', 'red', 'red', 'blue', 'black']
>>> 
>>> 
>>> 
>>> L = [1, 5, 8, 2, 3]
>>> L.sort()
>>> L
[1, 2, 3, 5, 8]
>>> 
>>> L = [1, 5, 8, 2, 3]
>>> L.sort(reverse=True)
>>> L
[8, 5, 3, 2, 1]
>>> 
>>> # --------------------------------- iterate
>>> 
>>> L = ['red', 'black', 'white', 'blue', 'red']
>>> for item in L:
	print(item)

	
red
black
white
blue
red
>>> 
