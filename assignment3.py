#!/usr/bin/env python
# coding: utf-8

# In[1]:


###NOTE: Some times list function does not work in jupyter note book , I have validate all the answers in pycharm  ###
   ###Ans 1 Print iNeuron###


# In[4]:


n = 5
for i in range(5):
    for j in range(0,i+1):
        print("iNeuron" , end = "  ")
    print("\n")


# In[5]:


###Ans 2 Print iNeuron in a dimond shape ###


# In[6]:


n= 3
space="       "
iNeuronSpace="iNeuron       "
for i in range(n):
  print(space* (n-i-1)+iNeuronSpace*(i+1) )
for j in range(n-1,0,-1):
  print(space*(n-j)+iNeuronSpace*(j))


# In[7]:


### Ans 3 Try to extract all the list entity###


# In[38]:


l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]


# In[40]:


l1=[]
for i in l :
    if type(i)==list:
        l1.append(i)
print(l1)


# In[ ]:


### Ans 4 Try to extract all the dict entityes###


# In[41]:


for i in l :
    if type(i)==dict:
        print(i)


# In[42]:


### Ans 5 Try to extract all the tuples entityes###


# In[43]:


for i in l :
    if type(i)==tuple:
        print(i)


# In[44]:


### Ans 6 Try to extract all the numarical data it may be a part of the dict key and value###


# In[45]:


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


# In[46]:


###Ans7 Try to give summation of all the numaric data###


# In[48]:


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
sum=0
for i in l1:
    sum=sum+i

print("sum:",sum)


# In[49]:


###Ans 8 Try to filter out all the odd values out all numaric data which is a part of a list###


# In[50]:


l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]
l1=[]
for i in l :
    if type (i) == list:
        for j in i:
            if type(j)==int and j%2 !=0:
                l1.append(j)
    if type (i) == tuple:
        for j in i:
            if type(j)==int and j%2 !=0:
                l1.append(j)
    if type (i) == set:
        for j in i:
            if type(j)==int and j%2 !=0:
                l1.append(j)
    if type(i) == dict:
        for k ,v in i.items():
            if type(k) == int and k%2 !=0:
                l1.append(k)
            if type(v) == int and v%2 !=0:
                l1.append(v)

print(l1)


# In[51]:


###Ans 9 Try to extract "ineuron" out of this data###


# In[52]:


l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' : "sudh" , "k2" : "ineuron" , "k3" : "kumar" , 3:6 , 7:8} , ["ineuron" , "data science"]]
l1=[]
for i in l :
    if type (i) == list:
        for j in i:
            if type(j)==str and j== "ineuron":
                l1.append(j)
    if type (i) == tuple:
        for j in i:
            if type(j)==str and j== "ineuron":
                l1.append(j)
    if type (i) == set:
        for j in i:
            if type(j)==str and j== "ineuron":
                l1.append(j)
    if type(i) == dict:
        for k ,v in i.items():
            if type(k) == str and k== "ineuron":
                l1.append(k)
            if type(v) == str and v== "ineuron":
                l1.append(v)

print(l1)


# In[53]:


###Ans 10Try to find out a number of occurance of all the data###


# In[54]:


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
s1= set(l1)
print(s1)
for i in s1:
    print("count of",i,":",l1.count(i))


# In[ ]:


###I will complete remaining 5 questions with assignment 4###

