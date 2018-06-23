Ques-1

"""
ArithmeticError 
"""
a=3
if a<4:
        try:
                a=a/(a-3)
                print(a)
        except(ArithmeticError):
                print("Exception handled")

Ques-2

"""
IndexError
"""
try:
        l=[1,2,3]
        print(l[3])
except(IndexError):
        print("Error handled")

Ques-3
"""
try:
    raise NameError("Hi there")
except NameError:
    print "An exception"
    raise
"""
Output:

An exception
Traceback (most recent call last):
  File "b.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there

Ques-4

"""
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
"""
Output:

-5.0
a/b result in 0

Ques-5


"""
1.ImportError
"""
from aaa import name

"""
Handle Error
"""
try:
        from aaa import name
except(ImportError):
        print("Error handled")

"""
2.ValueError
"""
int("abc")

"""
Handle Error
"""
try:
        int(input("Enter an integer: "))
except(ValueError):
        print("Error handled")

"""
3.IndexError
"""
list = [1,2,3,4]
print(list[5])

"""
Handle Error
"""
try:
        list = [1,2,3,4]
        print(list[0])
except(IndexError):
        print("Error handled")


Ques-6

class AgeTooSmallError(Exception):
        pass
while True:
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise AgeTooSmallError("Age should be greater than 18")
        else:
            print("You can continue")
            exit()

    except AgeTooSmallError:
        print("Age should be greater than 18")



