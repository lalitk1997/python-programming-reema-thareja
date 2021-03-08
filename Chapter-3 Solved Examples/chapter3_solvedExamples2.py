Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> str = 'Hello'
>>> print(str+'4')
Hello4
>>> print(str*5)
HelloHelloHelloHelloHello
>>> #slicing astring
>>> str = 'Python is easy !!'
>>> print(str)
Python is easy !!
>>> print(str[0])
P
>>> print(str[1:4])
yth
>>> print(str[4:])
on is easy !!
>>> print(str[-1])
!
>>> print(str * 2)
Python is easy !!Python is easy !!
>>> print(str + "Isn't it!")
Python is easy !!Isn't it!
>>> #data structure
>>> #tuple
>>> tup = (1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#')
>>> print(tup)
(1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#')
>>> print(tup * 2)
(1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#', 1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#')
>>> print(tup[0])
1
>>> print(tup[:3])
(1, 2, 3)
>>> tup1 = (6, 7, 8, 9, 0, 'g', 'h', 'ijk')
>>> print(tup1)
(6, 7, 8, 9, 0, 'g', 'h', 'ijk')
>>> print(tup1+tup)
(6, 7, 8, 9, 0, 'g', 'h', 'ijk', 1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#')
>>> print(tup + tup1)
(1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#', 6, 7, 8, 9, 0, 'g', 'h', 'ijk')
>>> tup2 = tup1 + tup
>>> print(tup2)
(6, 7, 8, 9, 0, 'g', 'h', 'ijk', 1, 2, 3, 4, 5, 'a', 'b', 'c', 'abcdefgh', '#')
>>> #lists
>>> #change change a value in between list
>>> list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
>>> print(list1)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
>>> print(list1[3:])
[4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
>>> print(list1[-1])
c
>>> list[0] = 'changed'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list[0] = 'changed'
TypeError: 'type' object does not support item assignment
>>> list1[0] = 'changed'
>>> print(list1)
['changed', 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
>>> list2 = [10, 11, 12, 13, 14, 15, 'd', 'e', 'f']
>>> list1 = list1 + list2
>>> print(list1)
['changed', 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 10, 11, 12, 13, 14, 15, 'd', 'e', 'f']
>>> #dictionaries
>>> dict1 = {'type':'dark choclate', 'price': 100}
>>> print(dict1['type'])
dark choclate
>>> print(dict1['price'])
100
>>> dict2 = {'type2':'vanilla flavor', 'price':80}
>>> dict1 + dict2
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict1 + dict2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> dict1 = dict1 + dict2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict1 = dict1 + dict2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> #type conversion
>>> '20' + '30'
'2030'
>>> 20 + 30
50
>>> int('20') + int('30')
50
>>> x = input('enter a number')
enter a number12
>>> y = input('enter another number')
enter another number21
>>> print(x+y)
1221
>>> print(int(x) + int(y))
33
>>> u = input(int('enter a number'))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    u = input(int('enter a number'))
ValueError: invalid literal for int() with base 10: 'enter a number'
>>> u = int(input('enter a number!'))
enter a number!12
>>> v = int(input('enter another number!))
	      
SyntaxError: EOL while scanning string literal
>>> v = int(input('enter another number!'))
enter another number!21
>>> print(u+v)
33
>>> print(str(u) + str(v))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(str(u) + str(v))
TypeError: 'str' object is not callable
>>> str(u)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    str(u)
TypeError: 'str' object is not callable
>>> u
12
>>> str(u)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str(u)
TypeError: 'str' object is not callable
>>> int(2.99)
2
>>> rount(2.99)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    rount(2.99)
NameError: name 'rount' is not defined
>>> round(2.99)
3
>>> 