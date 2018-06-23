Ques-1

"""
An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.
"""
create an applicatin on twitter>generate access token
 Access Token 783326174365745153-edVOBYIxgX2IUqUFkEXA28924V02Mjm 


Ques-2

import socket

address1 = socket.gethostbyname("www.facebook.com")
address2 = socket.gethostbyname("www.google.com")

print(address1)
print(address2)

Ques-3


#Import the necessary library, method, python file
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from auth import *
 
#This class is use for print tweet in json format
class StdOutListener(StreamListener):
 
    def on_data(self, data):
        try:
             
            jsonData = json.loads(data)
            text = jsonData['text'].lower() #In this statement we pick only text key value and convert it to lower form
            lang = jsonData['lang']#This statement fetch language of the tweet such as en,kl, etc.
            if lang=='en':
                if "rt" in text: #This if statement ignore the re-tweets using pass keyword
                    pass
                else:
                    txt=text.split("http")
                    print(txt[0]) #print the filter tweets 
                return True
 
        except:
            return True
    def on_error(self, status):
         print (status)
 
 
if __name__ == '__main__':
     
    #This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['delhi'])


Ques-4

A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case).

An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case).

Example:Angular js- a JS framework may use many libraries like iniline editing of text using an exposed API of that library.

