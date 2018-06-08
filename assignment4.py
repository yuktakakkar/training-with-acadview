TUPLES

Ques-1

a=(1,5,2,'a','b',6)
>>> print(a)
(1, 5, 2, 'a', 'b', 6)

>>> a=(1,2,6,5,76,111)
>>> print(a)
(1, 2, 6, 5, 76, 111)

Ques-1(1)

>>> a=(1,2,6,5,76,111)
>>> len(a)
6

Ques-2

>>> a=(1,2,6,5,76,111,0)
>>> max(a)
111
>>> min(a)
0

Ques-3

>>> x=(1,2,3,4,5)
>>> def mul():
...     unit_no=1
...     for a in x:
...             unit_no=unit_no*a
...     return unit_no
...
>>> print(mul())
120


SETS

Ques-1

>>> set1= set([1,2,3,4,5])
>>> set2 = set([4,5,6,7,8])
>>> print(set1)
{1, 2, 3, 4, 5}
>>> print(set2)
{4, 5, 6, 7, 8}

Ques-1(1)

>>> set1
{1, 2, 3, 4, 5}
>>> set2
{4, 5, 6, 7, 8}
>>> set1-set2
{1, 2, 3}
>>> set2-set1
{8, 6, 7}

Ques-1(2)
>>> set1
{1, 2, 3, 4, 5}
>>> set2
{4, 5, 6, 7, 8}
>>> if(set1 == set2):
...     print("Equal")
... else:
...     print("Unequal")
...
Unequal

>>> set1
{1, 2, 3, 4, 5}
>>> set2
{4, 5, 6, 7, 8}
>>> set1 == set2
False

Ques-1(3)

>>> set1
{1, 2, 3, 4, 5}
>>> set2
{4, 5, 6, 7, 8}
>>> set1 & set2
{4, 5}


DICTIONORIES

Ques-1

>>> name = 'q','w','e','r','t','y','u','i','o','p'
>>> marks = 45,12,65,44,98,11,57,90,43,15
>>> namemarks = {}
>>> y = 0
>>> for x in name:
...     namemarks[x] = marks[y]
...     y=y+1
...
>>> print(namemarks)
{'q': 45, 'w': 12, 'e': 65, 'r': 44, 't': 98, 'y': 11, 'u': 57, 'i': 90, 'o': 43, 'p': 15}

Ques-2

>>> import operator
>>> namemarks
{'q': 45, 'w': 12, 'e': 65, 'r': 44, 't': 98, 'y': 11, 'u': 57, 'i': 90, 'o': 43, 'p': 15}
>>> sort = sorted(namemarks.items(), key = operator.itemgetter(1))
>>> print(sort)
[('y', 11), ('w', 12), ('p', 15), ('o', 43), ('r', 44), ('q', 45), ('u', 57), ('e', 65), ('i', 90), ('t', 98)]

Ques-3

>>> import collections
>>> count = collections.Counter("MISSISSIPPI")
>>> print(count)
Counter({'I': 4, 'S': 4, 'P': 2, 'M': 1})