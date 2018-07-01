#Ques-1
//Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd



data  {'name': ['ankita'], 'age': [21], 'email': ['ankii123@abc.com'], 'phone_number': [9876543210]}

df = pd.DataFrame(data)



print(df)

#Ques2:
//Import the data and print the following :
a.) First 5 rows of Dataframe 
b.) First 10 rows of the Dataframe 
c.) find basic statistics on the particular dataset. 
d.) Find the last 5 rows of the dataframe 
e.) Extract the 2nd column and find basic statistics on it.

a.) import pandas as pd
>>> mydata= pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")
>>> mydata.head(5)

b.) import pandas as pd
>>> mydata= pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")
>>> mydata.head(10)

c.) >>> file = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv')
>>> file['MinTemp'].sum()
2659.2000000000003
>>> file['MinTemp'].describe()
count    366.000000
mean       7.265574
std        6.025800
min       -5.300000
25%        2.300000
50%        7.450000
75%       12.500000
max       20.900000
Name: MinTemp, dtype: float64
>>> file['MinTemp'].mean()
7.2655737704918044

d.) import pandas as pd
>>> mydata= pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")
>>> mydata.tail(5)

e.) import pandas as pd
>>> df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv')
df[2:3]
df[2:3].sum()
df[2:3].describe()
