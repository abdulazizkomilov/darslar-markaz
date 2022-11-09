nums = [5, 7, 2, 10, 0, 4, 9, 8, 6, 1, 3]

def bubble(nums):
    n = len(nums)
    swaps = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swaps += 1
    return swaps
          
def bubble_sort(nums):
    n = len(nums)
    for _ in range(n-1):
        if bubble(nums) == 0:
            break

bubble_sort(nums)