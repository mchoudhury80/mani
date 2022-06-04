#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Ans 11 Try to find out number of keys in dict element###

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]

for i in l:
    if type(i) == dict:
        print(i)
        for k in i.keys():
            print(k)


# In[2]:


###Ans 12 Try to filter out all the string data###

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]

l1=[]
for i in l :
    if type (i) == list:
        for j in i:
            if type(j)==str:
                l1.append(j)
    if type (i) == tuple:
        for j in i:
            if type(j)==str:
                l1.append(j)
    if type (i) == set:
        for j in i:
            if type(j)==str:
                l1.append(j)
    if type(i) == dict:
        for k ,v in i.items():
            if type(k) == str:
                l1.append(k)
            if type(v) == str:
                l1.append(v)

print(l1)


# In[3]:


###Ans 13 Try to find out alphanum in data###

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]
l1=[]
for i in l :
    if type (i) == list:
        for j in i:
             if type(j) == str and j.isalnum():
                l1.append(j)
    if type (i) == tuple:
         for j in i:
            if type(j) == str and j.isalnum():
                 l1.append(j)
    if type (i) == set:
         for j in i:
            if type(j) == str and j.isalnum():
                 l1.append(j)
    if type(i) == dict:
         for k ,v in i.items():
            if type(k) == str and k.isalnum():
                 l1.append(k)
            if type(v) == str and v.isalnum():
                 l1.append(v)

print(l1)


# In[4]:


###a14:Try to find out multiplication of all numaric value in the individual collection inside dataset###

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]
l1=[]
for i in l :
    if type (i) == list:
        for j in i:
            if type(j)==int:
                l1.append(j)
    if type (i) == tuple:
        for j in i:
            if type(j)==int:
                l1.append(j)
    if type (i) == set:
        for j in i:
            if type(j)==int:
                l1.append(j)
    if type(i) == dict:
        for k ,v in i.items():
            if type(k) == int:
                l1.append(k)
            if type(v) == int:
                l1.append(v)

print(l1)
mul=1
for i in l1:
    mul=mul*i

print("mul:",mul)



# In[5]:


###A15: Try to unwrap all the collection inside collection and creat a flat list###

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]
l1=[]
for i in l :
    if type (i) == list:
        for j in i:
                l1.append(j)
    if type (i) == tuple:
        for j in i:
                l1.append(j)
    if type (i) == set:
        for j in i:
                l1.append(j)
    if type(i) == dict:
        for k ,v in i.items():
                l1.append(k)
                l1.append(v)
print(l1)

