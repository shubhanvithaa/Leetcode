import heapq
nums = [3,2,3,1,2,4,5,5,6] 
k = 4
print( heapq.nlargest(k, nums)[-1])

#or through sorting

nums = [3,2,3,1,2,4,5,5,6] 
nums.sort(reverse = True)
k = 4
print(nums[k-1])