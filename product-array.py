nums = [1,2,3,4,5]
prod = []
for i in range(len(nums)):
    left = nums[:i]
    right = nums[i+1:]
    prodl = 1
    prodr = 1
    for l in left:
        prodl = l*prodl
    for j  in right:
        prodr = j*prodr
    prod.append(prodr*prodl)