Ques-1:

a = input("Enter a list: ")
Enter a list: a = [1, 2, "abc", [3, 4, "pqr"], "abc"]
>>> a
'a = [1, 2, "abc", [3, 4, "pqr"], "abc"]'

Ques-2:

 a.append(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
>>> a
[1, 2, 'abc', [3, 4, 'pqr'], 'abc', ['google', 'apple', 'facebook', 'microsoft', 'tesla']]

Ques-3:

>>> a.count(1)
1
>>> a.count(2)
1
>>> a.count('abc')
2
>>> a.count([3, 4, 'pqr'])
1
>>> a.count(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
1

Ques-4:

>>> b = [5, 3, 4, 7,1]
>>> b.sort()
>>> b
[1, 3, 4, 5, 7]

Ques-5:

>>> A = [[1, 2, 3], [4, 5, 6]]
>>> B=[[4, 3, 6], [7, 6, 9]]
>>> C = A + B
>>> C
[[1, 2, 3], [4, 5, 6], [4, 3, 6], [7, 6, 9]]
>>> C.sort()
>>> C
[[1, 2, 3], [4, 3, 6], [4, 5, 6], [7, 6, 9]]

Ques-6:

IMPLEMENTATION OF STACK:

>>> stack = [1, 2, 3, 4, 5]
>>> stack.append(10)
>>> stack
[1, 2, 3, 4, 5, 10]
>>> stack.pop()
10
>>> stack
[1, 2, 3, 4, 5]
>>> stack.pop()
5
>>> stack
[1, 2, 3, 4]

IMPLEMENTATION OF QUEUE:

>>> queue = [1, 2, 3, 4, 5]
>>> queue.append(10)
>>> queue
[1, 2, 3, 4, 5, 10]
>>> queue.pop(0)
1
>>> queue
[2, 3, 4, 5, 10]
>>> queue.pop(0)
2
>>> queue
[3, 4, 5, 10]

OPTIONAL QUESTION:

>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> even=0
>>> odd=0
>>> for x in numbers:
...     if x % 2 == 0:
...             even = even + 1
...     else:
...             odd = odd + 1
...
>>> print("Number of even numbers is",even)
Number of even numbers is 4
>>> print("Number of odd numbers is",odd)
Number of odd numbers is 5





