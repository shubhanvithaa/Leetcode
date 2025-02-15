class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = []
        zer = []
        for i in nums:
            if i != 0:
                res.append(i)
            else:
                zer.append(i)
        nums[:] = res + zer
