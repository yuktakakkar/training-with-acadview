Ques-1

>>> a = list(input("Enter 10 integers: "))
Enter 10 integers: 0123456789
>>> print(a)
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Ques-2

 i=1
>>> while(True):
...     print(i)
...
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1 and so on...

Ques-3

>>> a = list(input("Enter integers: "))
Enter integers: 12345
>>> a
['1', '2', '3', '4', '5']
>>> b = []
>>> for x in a:
...     b.append(int(x) ** 2)
...
>>> print(b)
[1, 4, 9, 16, 25]

Ques-4

a = [1,2,3.5,'s',4,'y',0.1]
integers = []
floats = []
strings = []
for x in range(len(a)):
     if type(a[x]) == int:
             integers.append(a[x])
     if type(a[x]) == float:
             floats.append(a[x])
     if type(a[x]) == str:
             strings.append(a[x])
print(integers)
print(floats)
print(strings)


[1, 2, 4]                                                                                                                        
[3.5, 0.1]                                                                                                                       
['s', 'y']

Ques-5

>>> for x in range(2,101,2):
...     print(x)
...
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100

>>> for x in range(1,101,2):
...     print(x)
...
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99

Ques-6

>>> def pattern(n):
...     for i in range(0,n):
...             for j in range(0,i+1):
...                     print("* ",end = " ")
...             print("\r")
...
>>> pattern(4)
*
*  *
*  *  *
*  *  *  *

Ques-7

>>> dict = {}
>>> dict[1] = 'a'
>>> dict[2] = 'b'
>>> dict[3] = 'c'
>>> dict[4] = 'd'
>>> print(dict)
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
>>> for i in dict.values():
...     a=dict.keys()
...
>>> print(a)
dict_keys([1, 2, 3, 4])

Ques-8

a = [1,2,3,4]
>>> b=4
>>> for x in a:
...     if b == a[x]:
...             a.remove(b)
...
>>> print(a)
[1, 2, 3]