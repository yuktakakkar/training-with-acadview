Ques-1

import threading
import time

def sleeper():
    print("Hi, I am going to sleep!")
    time.sleep(5)
    print("I am awake now!")

t = threading.Thread(sleeper())
t.start()

Ques-2

import threading
import time

def numbers():
    for i in range(1,11):
        print(i)
        time.sleep(1)

t = threading.Thread(numbers())
t.start()

Ques-3

import threading
import time

def lists(n):
    list = [1,2,3,4,5]
    for i in range(len(list)):
        print(list[i])
        time.sleep(n)
        n = n + 2

t = threading.Thread(lists(2))
t.start()

Ques-4

import threading
import time
import math

def factorial_fun(n):
    print(math.factorial(n))
    time.sleep(2)

t = threading.Thread(factorial_fun(5))
t.start()