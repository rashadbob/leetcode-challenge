list1=[1,2,4]
list2= [1,3,4]

s_a=[]
for i in range(len(list1)):
    
    for j in range(len(list2)):
        
             if list1[i] not in s_a and  list1[i]<list2[j]:
                s_a.append(list1[i])   


#print ("list1 :",list1)
#print ("list2 :",list2)
print(s_a)