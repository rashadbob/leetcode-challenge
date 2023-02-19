col_title="AB"
ct_list = list(col_title)

sheet_numb=[]

for i  in ct_list:
    
    
    sheet_numb.append(ord(i)-64)
    
    
s=[str(i) for i in sheet_numb]
print("".join(s))