class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        start = 0
        end = 0
        chance = 1
        i = start
        while(start < len(nums)-1 and i!= len(nums) ):
            if nums[i] == 1:
                count+=1
                i+=1
            else:
                chance-=1
                if chance == 0:
                    end = i
                i+=1
            if chance == -1:
                max_count = max(max_count , count)
                count = 0
                start = end + 1
                i = start
                chance = 1

        max_count = max(count,max_count)

        if len(nums) == 1 or sum(nums) == 0:
            return 0
        if sum(nums) == len(nums) or sum(nums) == len(nums) - 1:
            return nums-1
        return max_count