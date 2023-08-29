nums = [5, 7, 2, 10, 0, 4, 9, 8, 6, 1, 3]

def bubble(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] >= nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
          

print(bubble(nums))