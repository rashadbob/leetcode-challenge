

s = "()[]{}"

split_string = []

split_string.extend([*s])

for i in range(len(split_string)):
    print(ord(split_string[i]))
    if (ord(split_string[i])==(ord(split_string[i+1])-2)):
        print("test_success")



