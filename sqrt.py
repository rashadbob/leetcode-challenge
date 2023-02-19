

target_num=17

sqrt=0

for i in  range(1,target_num+1):
    if i*i == target_num:
        
        sqrt=sqrt+i
    
if sqrt>0:
    print("square root is ",sqrt)

else:
    print("no square root")