
def lcP():
    strs = ['flower','flight','flow']



    minlen = len(strs[0])

    for i in range(len(strs)):
        minlen=min(len(strs[i]),minlen)

   

    i=0 
    lcp="" 
    while i < minlen:
        char=strs[0][i] 
        print("char:",char)
        print("i",i)
        for j in range(len(strs)):
            print("j:",j)
            if strs[j][i] != char:
                return lcp

    
        lcp=lcp+char
        i += 1

    

    return lcp

print(lcP())
   



