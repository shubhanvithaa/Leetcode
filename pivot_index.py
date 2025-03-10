class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suml = 0
        sumr = sum(nums[1:])
        if suml == sumr:
            return 0
        for i in range(1,len(nums)):
            suml += nums[i-1]
            sumr -= nums[i]
            if suml == sumr:
                return i
        return -1