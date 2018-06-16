Ques-1

"""
Time tuple means in how many types a time can be displayed. It has many differe$
time.time()
time.gmtime()
time.asctime()
time.ctime()
"""

Ques-2

import time
time1 = time.asctime()
print(time1)

Ques-3

date1 = time1
day,month,date,time,year = date1.split(' ')
print(month) 

Ques-4

date1 = time1
day,month,date,time,year = date1.split(' ')
print(day)

Ques-5

date1 = time1
day,month,date,time,year = date1.split(' ')
print(date)

Ques-6

import time

time1 = time.localtime()
print(time1)

Ques-7

import math

number = int(input("Enter a number to find factorial: "))
factorial1 = math.factorial(number)
print(factorial1)

Ques-8

import math

number1 = int(input("Enter a number to find gcd: "))
number2 = int(input("Enter another number to find gcd: "))
gcd1 = math.gcd(number1,number2)
print(gcd1)

Ques-9

	1.
		import os
		print(os.getcwd())

	2.	os.environ
		
