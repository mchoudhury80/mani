#Ans 1
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l.reverse()
#print(l)
l1 = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#print(l1[::-1])
#Ans2 try to access 234 out of this list
l2 = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
t1 = l2[7]
#print(t1[0])
d1 = l2[8]
keysList=list(d1.keys())
#print(keysList[1])
#Ans3 try to access 456
l3 =[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#print(l3[5][1])
#Ans 4 . Try to extract only a list collection form list l
l4=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#print(l4[5:7])
#Ans5 . Try to extract "sudh"
l5=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l5Dist=l5.pop()
#print(l5Dist.get("key1"))
#Ans6 . Try to list all the key in dict element avaible in list
l6=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
dict=l6.pop()
#print(dict)
keys1=dict.keys()
#print(keys1)
keysList1=list(keys1)
#print(keysList1)
#Ans 7 . Try to extract all the value element form dict available in list
l7=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
dict1=l7.pop()
print(list(dict1.values()))




