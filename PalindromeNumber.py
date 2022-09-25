
from sre_constants import SUCCESS
from string import digits


target_number=16461


reversed_digits=[int(y) for y in str(target_number)]
digits=[]


while target_number > 0:

    digits.append(target_number % 10) #add right most digit to array 
    target_number = target_number - target_number % 10 # remove the right most digit from the number
    target_number = target_number //10 # divide by 10 (nnnnnn0/10= nnnnnnn)-> rm the 0 


res = all (digits[z] == reversed_digits[z] for z in range(len(digits)))
# we run an condition for every element within the digits array , bassically we check if each  digit is the same for the length of the number

if res == True:
    print('success')


print(digits)
print(reversed_digits)
