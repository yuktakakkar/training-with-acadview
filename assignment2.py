Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32

Ques-1:

>>> print('Acadview is the best')
Acadview is the best

Ques-2:

>>> print('Acad' + 'view')
Acadview
>>> a = print('Acad' + 'view')
Acadview
>>> a = 'Acad' + 'view'
>>> a
'Acadview'

Ques-3:

>>> input('x: ')
x: 3
'3'
>>> input('y: ')
y: 4
'4'
>>> input('z: ')
z: 5
'5'

Ques-4:

>>> print('Let/'s get started')                	//ERROR
  File "<stdin>", line 1                       	//ERROR  
    print('Let/'s get started')                	//ERROR
                ^                          	//ERROR
SyntaxError: invalid syntax			//ERROR


>>> print('Let\'s get started')
Let's get started

Ques-5:

>>> s="Acadview"
>>> course="Python"
>>> fees=5000
>>> sentence = '%s %d is %s'
>>> sentence%s						//ERROR
Traceback (most recent call last):			//ERROR
  File "<stdin>", line 1, in <module>			//ERROR
TypeError: not enough arguments for format string	//ERROR
>>> sentence%course					//ERROR
Traceback (most recent call last):                    	//ERROR
  File "<stdin>", line 1, in <module>			//ERROR
TypeError: not enough arguments for format string	//ERROR
>>> sentence = '%s %d is %s'				//ERROR
>>> sentence%(s,course,fees)				//ERROR
Traceback (most recent call last):			//ERROR
  File "<stdin>", line 1, in <module>			//ERROR
TypeError: %d format: a number is required, not str	//ERROR

>>> sentence = '%s %s is %d'
>>> sentence%(s,course,fees)	
'Acadview Python is 5000'

>>> sentence = 'Fees of %s for the course %s is %d'
>>> sentence%(s,course,fees)
'Fees of Acadview for the course Python is 5000'

Ques-6:

>>> name = 'Tony Stark'
>>> salary = 1000000

>>> print('%s"%d)%(name,salary)						//ERROR
  File "<stdin>", line 1						//ERROR
    print('%s"%d)%(name,salary)						//ERROR
                              ^						//ERROR
SyntaxError: EOL while scanning string literal				//ERROR
>>> print('%s"%d)%("Tony Stark",1000000)				//ERROR
  File "<stdin>", line 1						//ERROR
    print('%s"%d)%("Tony Stark",1000000)				//ERROR
                                       ^				//ERROR
SyntaxError: EOL while scanning string literal				//ERROR
>>> print('%s"%d)%('Tony Stark',1000000)				//ERROR
  File "<stdin>", line 1						//ERROR
    print('%s"%d)%('Tony Stark',1000000)				//ERROR
                       ^						//ERROR
SyntaxError: invalid syntax						//ERROR
>>> print('%s"%d')%('Tony Stark',1000000)				//ERROR
%s"%d									//ERROR
Traceback (most recent call last):					//ERROR
  File "<stdin>", line 1, in <module>					//ERROR
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'	//ERROR
>>> print('%s"%d')%(name,salary)					//ERROR
%s"%d									//ERROR
Traceback (most recent call last):					//ERROR
  File "<stdin>", line 1, in <module>					//ERROR
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'  	//ERROR
>>> print('%s"%d')%(name"salary)                                        //ERROR                             
  File "<stdin>", line 1						//ERROR
    print('%s"%d')%(name"salary)					//ERROR
                               ^					//ERROR
SyntaxError: EOL while scanning string literal				//ERROR
>>> print('%s"%d'%(name"salary))					//ERROR
  File "<stdin>", line 1						//ERROR
    print('%s"%d'%(name"salary))					//ERROR
                               ^					//ERROR
SyntaxError: EOL while scanning string literal				//ERROR


>>> print('%s"%d'%(name,salary))
Tony Stark"1000000
>>>