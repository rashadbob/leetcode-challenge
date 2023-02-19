
n=5
prev =2
prevprev=1
current=0

if n==1 or n==2:
    print("there",n,"ways to climb up the stairs") 

   
for i in range(3,n+1):
    current = prevprev + prev
    prevprev = prev
    prev = current


print(current)