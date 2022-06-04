#!/usr/bin/env python
# coding: utf-8

# In[2]:


###a1 : Try to print this by using while loop ###

print("right side angle triangle pattern")
i = 0
while i < 9:
    print('* '*(i+1))
    i= i+1


# In[3]:


###a2 : Try to print this by using while loop ###

print("right side angle triangle pattern")
n = 7
i = 0
while i < n:
    k = ord("A") +i
    count = 6
    j = 0
    while j < i + 1:
        if (k <= 90):
            print( chr(k), end= " " )
        k = k + count
        count = count-1
        j = j+1
    i = i+1

    print()


# In[ ]:


###a3 : Try to print all the number divisible by 3 in between a range of 40 - 400 by using while loop###

print("all the number divisible by 3")
i = 40
while i <= 400:
    if i%3 == 0:
        print(i)
    i+=1
    


# In[ ]:


###a3 : Try to print all the number divisible by 3 in between a range of 40 - 400 by using for loop###
print("all the number divisible by 3")
for i in range(40 , 400,1):
    if i%3 == 0:
        print(i)


# In[ ]:


###a4 : Try to filter out all the vowels form below text by using while loop###

str = """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]Python consistently ranks as one of the most popular programming languagesc"""
l = ["a","e","i","o","u","A","E","I","O","U"]
i = 0
while i < len(str):
    if l.__contains__(str[i]):
        print(str[i])
    i+=1


# In[ ]:


###a5 : Try to generate all the even number between 1- 1000 by using while loop###

while i <= 1000:
    if i % 2 == 0:
        print(i)
    i += 1


# In[ ]:


###a5 : Try to generate all the even number between 1- 1000 by using for loop###

for i in range(1 , 1000,1):
    if i%2 == 0:
        print(i)


# In[ ]:


###a6 : Define a function for all the above problem statememnt###

def extract_vowels():
    str = """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]Python consistently ranks as one of the most popular programming languagesc"""
    l = ["a","e","i","o","u","A","E","I","O","U"]
    i = 0
    while i < len(str):
         if l.__contains__(str[i]):
             print(str[i])
         i+=1


extract_vowels()


def star_triangle():
    i = 0
    while i < 9:
        print('* '*(i+1))
        i= i+1
star_triangle()



def alpha_triangle():
    n = 7
    i = 0
    while i < n:
        k = ord("A") +i
        count = 6
        j = 0
        while j < i + 1:
            if (k <= 90):
                print( chr(k), end= " " )
            k = k + count
            count = count-1
            j = j+1
        i = i+1

        print()
alpha_triangle()


def devisible_bythree():
    i = 40
    while i <= 400:
        if i % 3 == 0:
            print(i)
        i += 1
devisible_bythree()


def evev_number():
    for i in range(1, 1000, 1):
        if i % 2 == 0:
            print(i)
evev_number()


# In[5]:


###Q7:7 : write a code to get a time of your system ###

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("\nSystem Time is:", current_time)


# In[6]:


###A8: Write a code to fetch date form your system ###

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%m/%d/%Y")
print("\nSystem Time is:", current_time)


# In[ ]:


###a9 : Write a code to send a mail to your friend###

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "choudhury.rajesh@gmail.com"  # Enter your address
receiver_email = "choudhury.rajesh@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[ ]:


###q10 : write a code to trigger alarm for you at scheduled time ###

import datetime
import time
import winsound


def trigger_alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set timer is:",set_alarm_time)
        print(now)
        if now == set_alarm_time:
            print("Time to wake up zzzzzzzzzzzzzzzz")
            winsound.PlaySound("sound.way",winsound.SND_ASYNC)
            break
set_alarm_timer = input("Enter time to set alarm:")
trigger_alarm(set_alarm_timer)


# In[ ]:


###a11 : write a code to check ip address of your system ###

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Computer IP Address is:" + IPAddr)


# In[ ]:


###a12 : Write a code to check a perticular installation in your system###

import sys
if sys.version_info.major == 3:
    print('python3')
else:
    print('python2')


# In[ ]:


###a13 : Write a code to convert any text into voice###

import pyttsx3

engine = pyttsx3.init()

text = "Python consistently ranks as one of the most popular programming languagesc"
engine.say(text)
engine.runAndWait()


# In[ ]:


###a14 : you have to write a fun which will take string and return a len of it without using a inbuilt fun len###

my_string = "Python is a programming language"
print("The string is :")
print(my_string)
my_counter=0
for i in my_string:
   my_counter=my_counter+1
print("The length of the string is ")
print(my_counter)


# In[ ]:


###a15 :write a fun which will be able to print an index of all premitive element which you will pass###

def index_range(lst):
    print("List : ", lst)
    res = []
    for x in range (len(lst)):
        if lst[x] == 10:
            res.append(x)
    print("Index at which element 10 is present: " + str(res))

lst = [10, 20, 30, 10, 50, 10, 45, 10]
index_range(lst)


# In[ ]:


###q16 : Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work. ###

def dict_value(d1):
    d1.values()
    print(d1.values())
    l1=[]
    for i in d1.values():
        if type(i) == list:
            for j in i:
                l1.append(j)
        else:
            l1.append(i)
    print(l1)
d1 = {'name': 'Ravi', 'age': 23, 'marks': 56 ,'students' : [12,34,56,78,90]}
dict_value(d1)


# In[ ]:


###q17 : write a function whihc will take multiple list as a input and give me concatnation of all the element as and output###

def multiple_list(list1,list2,list3):
    for i in list2:
        list1.append(i)
    for i in list3:
        list1.append(i)
    print(list1)

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,12]
list3 = [13,14,15,16]
multiple_list(list1,list2,list3)


# In[ ]:




