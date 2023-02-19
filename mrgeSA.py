prices = [7,1,5,3,6,4]

buy_day = None # assign var null val
sell_day = None

for number in prices: # loop through array 
    if buy_day is None or number < buy_day:# is None or does the heavy lifting here 
        buy_day = number
        # basicallly for the first time we loop you have a none val  -> that cant be used in an int comparaison so until it has a val u use is none
print (buy_day)


bd=prices.index(buy_day)

for i in prices[bd:]:
    if sell_day is None or i > sell_day:
        sell_day = i

print(sell_day)

