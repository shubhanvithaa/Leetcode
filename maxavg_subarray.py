class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        first = nums[0]

        sums = float(sum(nums[:k]))
        length = len(nums)
        if length == k:
            max_sum = sums
        else:

            start = 1
            end = k
            max_sum = sums

            start_threshold = length-k

            if k ==1:
                max_sum = max(nums)
            else:

                while(start<start_threshold+1 and end <length+1 ):
                    sums = float(sums - first + nums[end])
                    max_sum = max(max_sum , sums)
                    first = nums[start]
                    end += 1
                    start += 1
        return max_sum/k

        