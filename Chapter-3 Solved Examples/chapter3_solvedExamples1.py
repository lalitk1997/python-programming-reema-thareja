Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 100;
>>> b = 200;
>>> +
SyntaxError: invalid syntax
>>> 
>>> print(a)
100
>>> print(b)
200
>>> print(a+b)
300
>>> print(a-b)
-100
>>> print(b/a)
2.0
>>> print(b%a)
0
>>> print(12//5)
2
>>> print(12.0 // 5.0)
2.0
>>> print(-19//5)
-4
>>> print(-22//5)
-5
>>> print(-23/5)
-4.6
>>> print(-23//5)
-5
>>> print(a**b)
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> print(a^b)
172
>>> print(-20//3.0)
-7.0
>>> #comparison operator
>>> a = 100;l
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = 100;l
NameError: name 'l' is not defined
>>> a = 100;
>>> b = 200;
>>> print(a == b)
False
>>> print(a != b)
True
>>> print(a < b)
True
>>> print(a > b)
False
>>> str1 = "Hello !"
>>> str2 = "Lalit Kumar!!"
>>> str1 += str2
>>> print("concatination : "+str1)
concatination : Hello !Lalit Kumar!!
>>> c = a;
>>> print(c)
100
>>>  a += b
 
SyntaxError: unexpected indent
>>> a += b
\
>>> print(a)
300
>>> a += b;
>>> print(b)
200
>>> print(b)
200
>>> print(a)
500
>>> print(a)
500
>>> print(b)
200
>>> b -= a
>>> print(b)
-300
>>> b *= a
>>> printf(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    printf(b)
NameError: name 'printf' is not defined
>>> print(b)
-150000
>>> a = 10;
>>> b = 100;
>>> c = 2;
>>> c **= b
>>> print(c)
1267650600228229401496703205376
>>> #unary operator
>>> # - (minus sign)
\
>>> a = 90
>>> print(-(a))
-90
>>> print(a)
90
>>> a = -a
>>> print(a)
-90
>>> a = -a
>>> print(a)
90
>>> #bitwise operator
>>> 101010 & 010101
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a = 101010
>>> b = 010101
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a = 10
>>> b = 4
>>> print(a & b)
0
>>> print(a | b)
14
>>> printf(a ^ b)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    printf(a ^ b)
NameError: name 'printf' is not defined
>>> print(a ^ b)
14
>>> print(~a)
-11
>>> #shift operators
>>> 16 << 1
32
>>> 16 >> 1
8
>>> a = 10
>>> b = 20
>>> c = 30
>>> (a < b) && (b < c)
SyntaxError: invalid syntax
>>> (a < b) and (b < c)
True
>>> (a > b) and (b < c)
False
>>> (a > b) or (b < c)
True
\
>>> a != b
True
>>> #membership operators
>>> #in operator and not in operator
>>> #identity operator
>>> a = 10
>>> b = 20
>>> b = a
>>> id(a)
1273721940560
>>> id(a) == id(b)
True
>>> #operator precedence and associativity
>>> 10 + 30 * 5
160
>>> print("python" + 3.4)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print("python" + 3.4)
TypeError: can only concatenate str (not "float") to str
>>> print("pyhton"+"3.4")
pyhton3.4
>>> "Hello" * 5
'HelloHelloHelloHelloHello'
>>> "Lalit Kumar " * 1000
'Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar Lalit Kumar '
>>> str1 = "Python is working"
print(str1)

