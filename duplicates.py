#finding duplicates.-- Time complexity o(n^2)


nums =  list(map(int, input("Enter numbers separated by space: ").split()))
count = 0
length = len(nums)
for i in range(length):
    for j in range(i+1,length):
        
        if nums[i] == nums[j]:
            count+=1
            break

    
if(count == 0):
    print("False")
else:
    print("True")
#solution 2

nums.sort()
length = len(nums)
for i in range(1,length):
    if nums[i] == nums[i-1]:
        print("True")
        break
    print("False")       



