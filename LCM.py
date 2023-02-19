

strs = ['flower','flight','flow']
print(len(strs))
a=''.join(strs)
b= str(a)#converts items to string 
print (b)
c=[] # holds indivual  16 letters from string
d=[]# holds matching letters  
e=[]#hold more than one lettersa
f=[]





for i in b:
    c.append(i)
        
        
for i in range(len(c)):
    for j in range (len(c)):
        if c[i]==c[j]:
          
            d.append(c[i])
                    
print (d)

for i in d :
    print (i,"appears",d.count(i),"times")
    if d.count(i)>=len(strs)*len(strs):
                
        e.append(i)
            
            
        
print ("e:",e)

for i in e:
    if i not in f :
        f.append(i)

print("f:",f)
print ("c:",c)        
                    
position=[]
""""
for i in range(len(c)):
    for j in f:
        if c[i]==j:
            position.append(i)
            print("matchj",c[i],"at index:",i)
#find repeated letter location in master string
"""
for i in f:
    for j in range(len(c)):
        if i==c[j]:
            print("letter",c[j],"is in positon",j)
            position.append(j)
#print("matching positions:",position)


print(position)



#two arrays
#one contains all reoccuring letters
#other contains all letters
#check positon of the first letter in the first array in the second array
#check postion of the second letter in the first array ion the second array 
#etc..
#add to array




















