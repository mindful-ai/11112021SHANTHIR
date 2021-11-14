Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'i', 'p', 'm', 's'}
>>> 
>>> 
>>> s1 = "abcdefgh"
>>> s1 = set(s1)
>>> s1
{'b', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> 
s
>>> s2 = {'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'}
>>> s1
{'b', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> s2
{'j', 'k', 'i', 'g', 'l', 'f', 'h', 'e'}
>>> 
>>> 
>>> # ---------------------- operators
>>> 
>>> s1
{'b', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> s2
{'j', 'k', 'i', 'g', 'l', 'f', 'h', 'e'}
>>> s1 & s2
{'f', 'g', 'h', 'e'}
>>> s1 | s2
{'b', 'j', 'k', 'a', 'i', 'g', 'd', 'l', 'c', 'f', 'h', 'e'}
>>> s1 ^ s2
{'b', 'j', 'k', 'i', 'a', 'l', 'd', 'c'}
>>> 
>>> s1.intersection(s2)
{'f', 'g', 'h', 'e'}
>>> s1.union(s2)
{'b', 'j', 'k', 'a', 'i', 'g', 'd', 'l', 'c', 'f', 'h', 'e'}
>>> 
>>> 
>>> # ------------------------ functions
>>> 
>>> s1
{'b', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> s1.add('x')
>>> s1
{'b', 'x', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> s1.add('x')
>>> s1
{'b', 'x', 'a', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> 
>>> s3 = {'x', 'y', 'z'}
>>> s3
{'z', 'x', 'y'}
>>> s1.update(s3)
>>> s1
{'b', 'y', 'x', 'a', 'z', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> 
>>> 'x' in s1
True
>>> s1.remove('x')
>>> s1
{'b', 'y', 'a', 'z', 'g', 'd', 'c', 'f', 'h', 'e'}
>>> 
>>> ''.join(s1)
'byazgdcfhe'
>>> 
