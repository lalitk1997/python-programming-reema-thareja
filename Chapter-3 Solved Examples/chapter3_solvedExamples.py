Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> "Hello World!"
'Hello World!'
>>> 91.5E2
9150.0
>>> float(16/float(3))
5.333333333333333
>>> format(float(16/float(3), '.2f'))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    format(float(16/float(3), '.2f'))
TypeError: float expected at most 1 argument, got 2
>>> format(float(16/float(3)), '.2f')
'5.33'
>>> format(3**50, '.5E')
'7.17898E+23'
>>> 15/0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    15/0
ZeroDivisionError: division by zero
>>> 5*3.0
15.0
>>> 78//5
15
>>> 121**0.5
11.0
>>> print('Hello!''...''Python')
Hello!...Python
>>> print('What\'s your name ?')
What's your name ?
>>> printf("The little boy replies, \"My name is Lalit \"")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    printf("The little boy replies, \"My name is Lalit \"")
NameError: name 'printf' is not defined
>>> print("The little boy replies, \"My name is Lalit \"")
The little boy replies, "My name is Lalit "
>>> print("My name is Lalit \t Kumar \n I am 23 years old")
My name is Lalit 	 Kumar 
 I am 23 years old
>>> print("\a")

>>> print(R "What\s your name?")
SyntaxError: invalid syntax
>>> print(R"What\'s your name")
What\'s your name
>>> print(R"What\s your name?")
What\s your name?
>>> format("Hello", "<30")
'Hello                         '
>>> format("Hello", ">30")
'                         Hello'
>>> format("Hello", "^30")
'            Hello             '
>>> print('Hello',format('-','-<10'), 'World')
Hello ---------- World
>>> print('Hello',format('.','-<10'), 'World')
Hello .--------- World
>>> format(123456789123456789, ',')
'123,456,789,123,456,789'
>>> num = 7
>>> amt = 123.45
>>> code = 'A'
>>> pi = 3.14159
>>> population_of_India = 1000000000
>>> msg = 'Ho'
>>> msg = 'Hi'
>>> print("Num = "+str(num))
Num = 7
>>> print("amt = "+str(amt))
amt = 123.45
>>> print("code = "+code)
code = A
>>> print("poplation_of_India = "+population_of_India)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("poplation_of_India = "+population_of_India)
TypeError: can only concatenate str (not "int") to str
>>> print("poplation_of_India = "+str(population_of_India))
poplation_of_India = 1000000000
>>> print('Msg = '+str(msg))
Msg = Hi
>>> val = 'Hello'
>>> print(val)
Hello
>>> val = 100
>>> print(val)
100
>>> val = 12.34
>>> print(val)
12.34
>>> x = 5;
>>> y = 10
>>> print("Hello")
Hello
>>> print(x+y)
15
>>> sum = flag = a = b = 0;
>>> printf("sum = "+str(sum))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    printf("sum = "+str(sum))
NameError: name 'printf' is not defined
>>> print("sum = "+str(sum))
sum = 0
>>> printf("flag = "+str(flag))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    printf("flag = "+str(flag))
NameError: name 'printf' is not defined
>>> print("flag = "+str(flag))
flag = 0
>>> sum, a, b, msg = 121, 12, 21, "hello"
>>> print("sum = "+str(sum))
sum = 121
>>> print("msg = "+str(msg))
msg = hello
>>> str = "Lalit Kumar"
>>> num = 10;
>>> age = 20
>>> print(str)
Lalit Kumar
>>> print(num)
10
>>> print(age)
20
>>> del(str)
>>> print(str)
<class 'str'>
>>> del(age)
>>> print(age)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(age)
NameError: name 'age' is not defined
>>> del(num)
>>> print(num)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(num)
NameError: name 'num' is not defined
>>> print(str)
<class 'str'>
>>> boolean_var = True
>>> boolean_var1 = False
>>> print(boolean_avr)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(boolean_avr)
NameError: name 'boolean_avr' is not defined
>>> print(boolean_var)
True
>>> "Hello " = "Hello "
SyntaxError: cannot assign to literal
>>> 
>>> "Hello" == "Hello"
True
>>> 2 != 3
True
>>> boolean_var && boolean_var1
SyntaxError: invalid syntax
>>> boolean_var & boolean_var1
False
>>> name = input("What's your name?")
What's your name?Lalit Kumar
>>> age = input("What is your age ?")
What is your age ?23
>>> printf("My name is "+(name)+"\n My age is "+(age))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    printf("My name is "+(name)+"\n My age is "+(age))
NameError: name 'printf' is not defined
>>> print("My name is "+(name)+"\n My age is "+(age))
My name is Lalit Kumar
 My age is 23
>>> # Comments start from using hash
>>> print("Hello Hi Bye") #Comments are ignored in all programming language
Hello Hi Bye
>>> # Arithematic operators
>>> a = 100;
>>> b = 200;
