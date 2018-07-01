#Ques-1
//Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy as np



a = np.random.rand(10,1)

print(a)



mean_of_elements = np.mean(a)

print("Mean =", mean_of_elements)

#Ques-2
//Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.

import numpy as np



a = np.random.rand(20,1)

print(a)



variance_of_elements = np.var(a)

print("Variance =", variance_of_elements)



standarddeviation = np.std(a)

print("Standard Deviation = ", standarddeviation)

#Ques-3
//Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

import numpy as np



A = np.random.rand(10,20)

print(A)



B = np.random.rand(20,25)

print(B)



C = np.dot(A,B)

print(C)



print(C.shape)



print(np.sum(C))

#Ques-4
//Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A. 
f(x)=1 / (1 + exp(-x)) 

import numpy as np

A = np.random.rand(10,1)
print (A)

def func(x):
    return (1 / (1 + np.exp(-x)))
    
function = np.apply_along_axis(func, 0, A)
print(function)
