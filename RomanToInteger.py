print ('please enter your roman numeral')

user_roman_numeral =input()

print ('the roman numeral is ' + user_roman_numeral)

my_charecters ={
'I': 1,
'V':5,
'X': 10,
'L':50,
'C':100,
'D':500,
'M':1000,
}
roman_value=[]

roman_value.extend([*user_roman_numeral.upper()])

placeholders=[]

test_success=[]
placeholders.extend(['M','C','D','L','X','V','I'])

for i in range(len(roman_value)):
    for j in range(len(placeholders)):
        print('test')
        if roman_value[i] == placeholders[j]:
            print('success')
            test_success.append(placeholders[j])



print (placeholders)

print (roman_value)

print(test_success)

total_sum =0

for i in range (len(test_success)):
    total_sum=total_sum+(my_charecters[test_success[i]])


print(total_sum)
