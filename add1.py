class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num = num*10+i
        num = num + 1
        print(num)
        res = list(map(int, str(num)))
        return res