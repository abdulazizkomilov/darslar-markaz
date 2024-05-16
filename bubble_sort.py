nums = [5, 7, 2, 10, 0, 4, 9, 8, 6, 1, 3]


def bubble(nums):
    n = len(nums)
    for j in range(n-1):
        next_ = False
        for i in range(n-j-1):
            if nums[i] >= nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                next_ = True
                
        if not next_:
            break
    return nums
          
print(bubble(nums))

