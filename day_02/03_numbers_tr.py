Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers => Numeric Values
>>> 
>>> # Operators
>>> # --------------------- Arithmetic Operators
>>> 
>>> a = 5
>>> b = 2
>>> A= b
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a // b
2
>>> a % b
1
>>> 8 % 6
2
>>> a ** 2
25
>>> 
>>> # ---------------------- Relational operators
>>> 
>>> a > 5 # Is a gretaer than 5? NO
False
>>> a < 5
False
>>> a == 5
True
>>> a >= 5
True
>>> a <= 5
True
>>> myValue = True
>>> type(myValue)
<class 'bool'>
>>> m = False
>>> type(m)
<class 'bool'>
>>> 
>>> 
>>> # ---------------------------- Logical Operators
>>> 
>>> a < b and a > 10
False
>>> a
5
>>> b
2
>>> a > b and a > 10
False
>>> a > b and a <= 5
True
>>> a > b or a > 10
True
>>> a > b or not a > 10
True
>>> a > b and not a > 10
True
>>> 
>>> # ----------------------------- in-built functions
>>> 
>>> a - b
3
>>> b - a
-3
>>> abs(b - a)
3
>>> abs(a - b
    )
3
>>> a = 100
>>> type(a)
<class 'int'>
>>> float(a)
100.0
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> bin(a)
'0b1100100'
>>> 
>>> pow(5, 2)
25
>>> s = '10111001'
>>> int(s)
10111001
>>> int(s) + 1
10111002
>>> # 1010 => 10, 1011 => 11, 1100 => 12
>>> int(s, 2)
185
>>> 
>>> # --------------------------- built in modules
>>> 
>>> 
>>> a = 100
>>> 
>>> sqrt(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sqrt(a)
NameError: name 'sqrt' is not defined
>>> import math
>>> sqrt(a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    sqrt(a)
NameError: name 'sqrt' is not defined
>>> math.sqrt(a)
10.0
>>> 
>>> 
>>> a = 90
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> b = math.radians(90)
>>> math.sin(b)
1.0
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_02/02_ex_solution.py ===
Calculate Height of a building using elevation angle
Enter the distance from the building40
Enter angle of elevation45
Height is  39.99999999999999
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_02/02_ex_solution.py ===
Calculate Height of a building using elevation angle
Enter the distance from the building45.5
Enter angle of elevation56.76
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/shanthi/day_02/02_ex_solution.py", line 19, in <module>
    height=math.tan(int(ang)*math.pi/180)*int(dist)
ValueError: invalid literal for int() with base 10: '56.76'
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/shanthi/day_02/02_ex_solution.py ===
Calculate Height of a building using elevation angle
Enter the distance from the building45.6
Enter angle of elevation56.76
Height is  69.57803950269792
>>> 
