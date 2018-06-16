Ques-1

class Circle():
        def __init__(self,radius):
                self.radius = radius
        def getArea(self):
                return(3.14 * (self.radius ** 2))
        def getCircumference():
                return(2 * 3.14 * self.radius)

Ques-2


class Student():
        def __init__(self, name, rollno):       
                self.name = name
                self.rollno = rollno
        def display(self):
                print self.name
                print self.rollno

Ques-3

class Temprature():
        def convertFahrenheit(self,celcius):
             	return(self.celsius*(9/5))+32
        def convertCelcius(self,fahrenheit):
                return(farenhiet-32)*(5/9)

Ques-4

class MovieDetails():
        def __init__(self, moviename, artistname, yearofrelease,$
                self.moviename = moviename
                self.artistname = artistname
                self.yearofrelease = yearofrelease
                self.ratings = ratings
        def display(self):
                print(self.moviename)
                print(self.artistname)
                print(self.yearofrelease)
                print(self.ratings)
        def update(self):
                print(self.moviename.update('a'))
                print(self.artistname.update('b'))
                print(self.yearofrelease.update(2015))
                print(self.ratings(3))

Ques-5

class Expenditure():
        def __init__(self, expenditure, savings):
                self.expenditure = expenditure
                self.savings = savings
        def display(self):
                print(self.expenditure)
                print(self.savings)
        def total_salary(self):
                return( self.basic + self.HRA + self.DA + self.MA)


