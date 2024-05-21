array = [4, 6, 1, 9]

def func(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(func(array))




# list_1 = [1,2,3,4,5,6,8,9,10,12]

# def find(nums: list[int]) -> int:
#     N = len(nums)+1
#     sumE = N*(N+1)/2
#     sumA = sum(nums)
    
#     return sumE-sumA

# print(find(list_1))
