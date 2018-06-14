Ques-1

>>> pi = 3.142
>>> def area(r):
...     return(pi * r * r)
...
>>> r = int(input("Enter radius: "))
Enter radius: 4
>>> print("Area is: ",area(r))
Area is:  50.272

Ques-2

>>> def perfect(n):
...     sum=0
...     for i in range(1,n):
...             if n % i == 0:
...                     sum = sum + i
...     if sum == n:
...             return True
...     else:
...             return False
>>> for i in range(1,1000):
...     if perfect(i):
...             print(i, end=" ")
...
6 28 496

Ques-3

>>> def mul_table(n,t=1):
...     if t == 11:
...             return False
...     else:
...             print(n * t)
...             mul_table(n, t+1)
...
>>> n = int(input("Enter number: "))
Enter number: 12
>>> mul_table(n)
12
24
36
48
60
72
84
96
108
120

Ques-4

>>> def power(a, b):
...     if b == 1:
...             return a
...     else:
...             return(a *power(a, b-1))
...
>>> a = int(input("Enter base: "))
Enter base: 2
>>> b = int(input("Enter power: "))
Enter power: 3
>>> power(a,b)
8
