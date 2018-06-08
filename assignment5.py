Ques-1

>>> year =int(input("Enter a year: "))
Enter a year: 2012
>>> if year%4 == 0:
...     if year%100 == 0:
...             if year%400 == 0:
...                     print("Leap year")
...             else:
...                     print("Not a leap year")
...     else:
...             print("Leap year")
... else:
...     print("Not a leap year")
...
Leap year

Ques-2

>>> length = int(input("Enter length: "))
Enter length: 6
>>> breadth = int(input("Enter breadth: "))
Enter breadth: 4
>>> if length == breadth:
...     print("Dimensions are of square")
... else:
...     print("Dimensions are of rectangle")
...
Dimensions are of rectangle

Ques-3

Oldest:

>>> age1 = int(input("Enter age of 1st person: "))
Enter age of 1st person: 32
>>> age2 = int(input("Enter age of 2nd person: "))
Enter age of 2nd person: 45
>>> age3 = int(input("Enter age of 3rd person: "))
Enter age of 3rd person: 21
>>> if age1 > age2:
...     if age1 > age3:
...             print("Oldest is: ",age1)
...     else:
...             print("Oldest is: ",age3)
... elif age2 > age3:
...     print("Oldest is: ",age2)
... else:
...     print("Oldest is: ",age3)
...
Oldest is:  45

Youngest:

>>> age1 = int(input("Enter age of 1st person: "))
Enter age of 1st person: 32
>>> age2 = int(input("Enter age of 2nd person: "))
Enter age of 2nd person: 45
>>> age3 = int(input("Enter age of 3rd person: "))
Enter age of 3rd person: 21
>>> if age1 < age2:
...     if age1 < age3:
...             print("Youngest is: ",age1)
...     else:
...             print("Youngest is: ",age3)
... elif age2 < age3:
...     print("Youngest is: ",age2)
... else:
...     print("Youngest is: ",age3)
...
Youngest is:  21

Ques-4

>>> points = int(input("Points: "))
Points: 210
>>> if 1 < points < 50:
...     print("Sorry! No prize this time")
... elif 51 < points < 150:
...     print("Congratulations! You won a Wooden Dog!")
... elif 150 < points < 180:
...     print("Congratulations! You won a Book!")
... elif 181 < points < 200:
...     print("Congratulations! You won Chocolates!")
... else:
...     print("Points are invalid")
...
Points are invalid

>>> points = int(input("Points: "))
Points: 149
>>> if 1 < points < 50:
...     print("Sorry! No prize this time")
... elif 51 < points < 150:
...     print("Congratulations! You won a Wooden Dog!")
... elif 150 < points < 180:
...     print("Congratulations! You won a Book!")
... elif 181 < points < 200:
...     print("Congratulations! You won Chocolates!")
... else:
...     print("Points are invalid")
...
Congratulations! You won a Wooden Dog!

Ques-5

>>> price = int(input("Enter price: "))
Enter price: 2000
>>> if price <= 1000:
...     print("Sorry! No discount on the purchase")
...     print("You have to pay: ",price)
... else:
...     print("Congratulations! You get 10% discount on your purchase")
...     discount = price * float(0.1)
...     total = price - discount
...     print("You have to pay: ",total)
...
Congratulations! You get 10% discount on your purchase
You have to pay:  1800.0

>>> price = int(input("Enter price: "))
Enter price: 900
>>> if price <= 1000:
...     print("Sorry! No discount on the purchase")
...     print("You have to pay: ",price)
... else:
...     print("Congratulations! You get 10% discount on your purchase")
...     discount = price * float(0.1)
...     total = price - discount
...     print("You have to pay: ",total)
...
Sorry! No discount on the purchase
You have to pay:  900