nums=[1,2,2,1,3,3,4,4,4,6]



for i in nums:
    
   
        #    print("nums befor cal:",nums)

            while nums.count(i) > 1:
                nums.remove(i)

print(nums)