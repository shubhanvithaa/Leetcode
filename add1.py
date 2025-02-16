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
    #or dolution-2

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # Start from the last digit
            if digits[i] < 9:  # If digit is not 9, just add 1 and return
                digits[i] += 1
                return digits
            digits[i] = 0  # If digit is 9, set to 0 and continue
        
        # If all digits were 9, we need an extra digit at the beginning (e.g., 999 -> 1000)
        return [1] + digits

# Example Usage
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]

