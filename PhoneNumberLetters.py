#FAILED DOESN'T WORK
nmbrs = "23"

n_t= list(nmbrs)

print (n_t)
test_dict = {
    '2':"abc",'3':"def",
    '4':"ghi",'5':"jkl",
    '6':"mno",'7':"pqrs",
    '8':"tuv",'9':"wxyz"
}

mtch = []
letters=[]

for i in test_dict:
    for j in n_t:
        if i == j:
            mtch.append(test_dict[i])
#        print(i,test_dict[i])


print (mtch)
for i in range(len(mtch)):
    letters.append(list(mtch[i]))

res_let= sum(letters,[])   
    


print(res_let)
combonations =[]
for i in res_let:
    for j in res_let:
        if i != j:
            print([i,j])
#print (s_c)

print (combonations)