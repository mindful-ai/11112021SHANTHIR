Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS AND OPERATIONS ON STRINGS
>>> 
>>> s = "computer"
>>> 
>>> # ------------------ indexes
>>> 
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[2]
'm'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> s[-3]
't'
>>> s[3:5]
'pu'
>>> s[3:6]
'put'
>>> len(s)
8
>>> s[3:8]
'puter'
>>> s[3:7]
'pute'
>>> s[3:9]
'puter'
>>> s[3:-1]
'pute'
>>> s[-4:-1]
'ute'
>>> s[0:5]
'compu'
>>> s[:5]
'compu'
>>> s[4:8]
'uter'
>>> s[4:]
'uter'
>>> s[:]
'computer'
>>> s[1:5]
'ompu'
>>> s[1:5:2]
'op'
>>> s[::2]
'cmue'
>>> s[::3]
'cpe'
>>> s[::-1]
'retupmoc'
>>> s[::-2]
'rtpo'
>>> s[1:7]
'ompute'
>>> s[1:7:-1]
''
>>> s[1:7][::-1]
'etupmo'
>>> 
>>> # -------------------------- immutability
>>> 
>>> s
'computer'
>>> s[3]
'p'
>>> s[3] = 'k'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s[3] = 'k'
TypeError: 'str' object does not support item assignment
>>> 
>>> s = 'python'
>>> s
'python'
>>> s[3]
'h'
>>> s[3] = 'r'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s[3] = 'r'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ---------------------------- operators
>>> 
>>> 'abcd' + 'efgh'
'abcdefgh'
>>> 
>>> 'abc' * 3
'abcabcabc'
>>> 
>>> len('abc')
3
>>> 'b' in 'abc'
True
>>> 'v' in 'abc'
False
>>> 
>>> 'abc' is str
False
>>> type('abc') is str
True
>>> type(10) is int
True
>>> 
>>> 'abc' == str
False
>>> 'abc' == 'def'
False
>>> 'abc' == 'abc'
True
>>> if 'abc' == 'abc':
	print("They areequal")

	
They areequal
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
s
>>> s = 10
>>> s ='abc'
>>> 
>>> # ---------------------------- functions
>>> 
>>> s = "computer"
>>> 
>>> 
>>> # ----- G1: cases
>>> 
>>> s.upper()
'COMPUTER'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> i = 10
>>> dir(i)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> abs(10)
10
>>> 10.abs()
SyntaxError: invalid syntax
>>> x = 10.5
>>> x.numerator()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    x.numerator()
AttributeError: 'float' object has no attribute 'numerator'
>>> i
10
>>> i.numerator()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    i.numerator()
TypeError: 'int' object is not callable
>>> numerator(i)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    numerator(i)
NameError: name 'numerator' is not defined
>>> import Fraction
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    import Fraction
ModuleNotFoundError: No module named 'Fraction'
>>> Fraction()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    Fraction()
NameError: name 'Fraction' is not defined
>>> import fraction
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    import fraction
ModuleNotFoundError: No module named 'fraction'
>>> 
>>> 
>>> a = 5
>>> b = 6
>>> a <= 4
False
>>> a = "a"
>>> b = "b"
>>> type(a)
<class 'str'>
>>> a == b
False
>>> a <= b
True
>>> i = 100
>>> i.bit_length()
7
>>> f = 1/5
>>> f.numerator()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    f.numerator()
AttributeError: 'float' object has no attribute 'numerator'
>>> numerator(f)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    numerator(f)
NameError: name 'numerator' is not defined
>>> 
>>> 
>>> 
>>> # --------------------- G2: Checking
>>> 
>>> s = "123454"
>>> s.isdigit()
True
>>> s.isalpha()
False
>>> s.isalnum()
True
>>> 'ABC123'.isalnum()
True
>>> '%$ABC123'.isalpha()
False
>>> '    '.isspace()
True
>>> 
>>> site = "www.google.com"
>>> site.startswith("https")
False
>>> site.endswith("com")
True
>>> text = "This Is Python Course"
>>> text.istitle()
True
>>> site.istitle()
False
>>> 
>>> 
>>> # ------------------ G3: searching
>>> 
>>> s
'123454'
>>> s = "computer"
>>> 'put' in s
True
>>> s.index('put')
3
>>> s = "mississississippi"
>>> s.index('ss')
2
>>> s.find('ss')
2
>>> s.rindex('ss')
11
>>> 
>>> 
>>> # ------------------ G4: modificaitons
>>> 
>>> ip = '56-56-32-12'
>>> ip.replace('-', '.')
'56.56.32.12'
>>> ip
'56-56-32-12'
>>> 
>>> # --- strip
>>> 
>>> m = '   hello  ''
SyntaxError: EOL while scanning string literal
>>> m = '   hello  '
>>> m.strip()
'hello'
>>> m.lstrip()
'hello  '
>>> m.rstrip()
'   hello'
>>> 
>>> 
>>> # justification
>>> m
'   hello  '
>>> p = m.strip()
>>> m
'   hello  '
>>> p
'hello'
>>> 
>>> 
>>> p
'hello'
>>> p.rjust(20)
'               hello'
>>> p.ljust(20)
'hello               '
>>> p.ljust(20, '>')
'hello>>>>>>>>>>>>>>>'
>>> 
>>> 
>>> 
>>> # split, join
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> 
>>> L = ['mary', 'had', 'a', 'little', 'lamb']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 
>>> 
>>> # -------------------- format
>>> 
>>> print('My name is Nikhil and age is 35')
My name is Nikhil and age is 35
>>> 
>>> name = 'Nikhil'
>>> age = 35
>>> 
>>> print('My name is', name, ' and age is ', age)
My name is Nikhil  and age is  35
>>> print('My name is %s and age %d' % (name, age))
My name is Nikhil and age 35
>>> print('My name is %s %s and age %d' % (name, 'Kumar', age))
My name is Nikhil Kumar and age 35
>>> print('My name is %s %s and age %d' , (name, 'Kumar', age))
My name is %s %s and age %d ('Nikhil', 'Kumar', 35)
>>> print('My name is {} {} and age {}'.format(name, 'Kumar', age))
My name is Nikhil Kumar and age 35
>>> print('My name is {0} {1} and age {2}'.format(name, 'Kumar', age))
My name is Nikhil Kumar and age 35
>>> print('My name is {1} {0} and age {2}'.format(name, 'Kumar', age))
My name is Kumar Nikhil and age 35
>>> print('My name is {1:10} {0:8} and age {2:5}'.format(name, 'Kumar', age))
My name is Kumar      Nikhil   and age    35
>>> print('My name is {1:>10} {0:<8} and age {2:^5}'.format(name, 'Kumar', age))
My name is      Kumar Nikhil   and age  35  
>>> 
