nums=[2,12,8,7]

target =9


output =[]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] +nums[j] == target:
            output.append(i)
            

print (output)



#leet code version
'''''
class Solution(object):
    
   

    def twoSum(self, nums, target):
      
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] +nums[j] == target:
                    return [i,j]
    
'''''