

str1= "123"
str2 = "45654"

strs = []

strs.append(str1)
strs.append(str2)


print(str1,str2)

new_num=[]
for i in strs:
    new_num.append(int(i,base=10))

res=1

for x in new_num:
    res= res*x

print (res)

