#finding duplicates.

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