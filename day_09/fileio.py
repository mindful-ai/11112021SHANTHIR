Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Text file read/write
>>> 
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # tell(), seek()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\shanthi\day_09\data.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> p = "C:\text\read\next\all.dat"
>>> print(p)
C:	extead
extll.dat
>>> p = r"C:\text\read\next\all.dat"
>>> print(p)
C:\text\read\next\all.dat
>>> path = r"C:\Users\Purushotham\Desktop\shanthi\day_09\data.txt"
>>> 
>>> 
>>> # ------------------- open a file
>>> 
>>> f = open(path, mode='b') # mode -> r, w, a, b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f = open(path, mode='b') # mode -> r, w, a, b
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> f = open(path, 'r')
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\shanthi\\day_09\\data.txt' mode='r' encoding='cp1252'>
>>> 
>>> # -------------------- read a file
>>> 
>>> f.read()
'You shall find of the king a husband, madam; you,\nsir, a father: he that so generally is at all times\ngood must of necessity hold his virtue to you; whose\nworthiness would stir it up where it wanted rather\nthan lack it where there is such abundance.'
>>> print(f.read())

>>> f.tell()
253
>>> f.seek(0)
0
>>> print(f.read())
You shall find of the king a husband, madam; you,
sir, a father: he that so generally is at all times
good must of necessity hold his virtue to you; whose
worthiness would stir it up where it wanted rather
than lack it where there is such abundance.
>>> f.seek(0)
0
>>> text = f.read()
>>> text
'You shall find of the king a husband, madam; you,\nsir, a father: he that so generally is at all times\ngood must of necessity hold his virtue to you; whose\nworthiness would stir it up where it wanted rather\nthan lack it where there is such abundance.'
>>> type(text)
<class 'str'>
>>> len(str)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(str)
TypeError: object of type 'type' has no len()
>>> len(text)
249
>>> t = "abc def"
>>> len(t)
7
>>> t = "abc\ndef"
>>> len(t)
7
>>> print(t)
abc
def
>>> t = '''abc
def'''
>>> t
'abc\ndef'
>>> len(t)
7
>>> f.seek(0)
0
>>> f.read(10)
'You shall '
>>> f.read(10)
'find of th'
>>> f.read(10)
'e king a h'
>>> f.tell()
30
>>> f.seel(11)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    f.seel(11)
AttributeError: '_io.TextIOWrapper' object has no attribute 'seel'
>>> f.seek(11)
11
>>> f.read(10)
'ind of the'
>>> 
>>> 
>>> # ----------------------- readline()
>>> 
>>> f.seek()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    f.seek()
TypeError: seek() takes at least 1 argument (0 given)
>>> f.seek(0)
0
>>> f.readline()
'You shall find of the king a husband, madam; you,\n'
>>> f.readline()
'sir, a father: he that so generally is at all times\n'
>>> f.read(10)
'good must '
>>> 
>>> # --------------------------- readlines()
>>> 
>>> f.seek(0)
0
>>> f.readlines()
['You shall find of the king a husband, madam; you,\n', 'sir, a father: he that so generally is at all times\n', 'good must of necessity hold his virtue to you; whose\n', 'worthiness would stir it up where it wanted rather\n', 'than lack it where there is such abundance.']
>>> f.seek(0)
0
>>> c = f.readlines()
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
>>> c[0]
'You shall find of the king a husband, madam; you,\n'
>>> c[1]
'sir, a father: he that so generally is at all times\n'
>>> c[2:3]
['good must of necessity hold his virtue to you; whose\n']
>>> c[::-1]
['than lack it where there is such abundance.', 'worthiness would stir it up where it wanted rather\n', 'good must of necessity hold his virtue to you; whose\n', 'sir, a father: he that so generally is at all times\n', 'You shall find of the king a husband, madam; you,\n']
>>> 
>>> # -------------------------- closeing the file
>>> 
>>> f.close()
>>> 
>>> # -------------------------- open the file in write mode
>>> 
>>> path = r"C:\Users\Purushotham\Desktop\shanthi\day_09\data2.txt"
>>> f = open(path, 'w')
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\shanthi\\day_09\\data2.txt' mode='w' encoding='cp1252'>
>>> 
>>> f.write("Shakespere\n")
11
>>> f.write("Newly created file \n")
20
>>> f.close()
>>> 
>>> # --------------------------- open the file in the append mode
>>> 
>>> f = open(path, 'a')
>>> c
['You shall find of the king a husband, madam; you,\n', 'sir, a father: he that so generally is at all times\n', 'good must of necessity hold his virtue to you; whose\n', 'worthiness would stir it up where it wanted rather\n', 'than lack it where there is such abundance.']
>>> 
>>> cr = c[::-1]
>>> f.writelines(cr)
>>> 
>>> f.close()
>>> 
>>> # ---------------------------- writing a word histogram
>>> 
>>> # red red green
>>> # red -> 2, green -> 1
>>> 
>>> text
'You shall find of the king a husband, madam; you,\nsir, a father: he that so generally is at all times\ngood must of necessity hold his virtue to you; whose\nworthiness would stir it up where it wanted rather\nthan lack it where there is such abundance.'
>>> words = text.split()
>>> words
['You', 'shall', 'find', 'of', 'the', 'king', 'a', 'husband,', 'madam;', 'you,', 'sir,', 'a', 'father:', 'he', 'that', 'so', 'generally', 'is', 'at', 'all', 'times', 'good', 'must', 'of', 'necessity', 'hold', 'his', 'virtue', 'to', 'you;', 'whose', 'worthiness', 'would', 'stir', 'it', 'up', 'where', 'it', 'wanted', 'rather', 'than', 'lack', 'it', 'where', 'there', 'is', 'such', 'abundance.']
>>> 
>>> D = {}
>>> for word in words:
	if word in D.keys():
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'You': 1, 'shall': 1, 'find': 1, 'of': 2, 'the': 1, 'king': 1, 'a': 2, 'husband,': 1, 'madam;': 1, 'you,': 1, 'sir,': 1, 'father:': 1, 'he': 1, 'that': 1, 'so': 1, 'generally': 1, 'is': 2, 'at': 1, 'all': 1, 'times': 1, 'good': 1, 'must': 1, 'necessity': 1, 'hold': 1, 'his': 1, 'virtue': 1, 'to': 1, 'you;': 1, 'whose': 1, 'worthiness': 1, 'would': 1, 'stir': 1, 'it': 3, 'up': 1, 'where': 2, 'wanted': 1, 'rather': 1, 'than': 1, 'lack': 1, 'there': 1, 'such': 1, 'abundance.': 1}
>>> f = open(path, 'a')
>>> f.write("\n")
1
>>> for key in D.keys():
	s = key + ' -> ' + D[key] + '\n'
	f.write(s)

	
Traceback (most recent call last):
  File "<pyshell#120>", line 2, in <module>
    s = key + ' -> ' + D[key] + '\n'
TypeError: can only concatenate str (not "int") to str
>>> for key in D.keys():
	s = key + ' -> ' + str(D[key]) + '\n'
	f.write(s)

	
9
11
10
8
9
10
7
14
12
10
10
13
8
10
8
15
8
8
9
11
10
10
15
10
9
12
8
10
11
16
11
10
8
8
11
12
12
10
10
11
10
16
>>> f.close()
>>> 
