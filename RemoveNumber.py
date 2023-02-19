


nums=[3,2,2,3]
val=3

while val in nums:
    for i in nums:
        if i == val:
            nums.remove(i)

    print("nums:",nums)