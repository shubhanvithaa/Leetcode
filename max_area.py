class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = 0
        area = 0

        while(left != right):
            if height[left] < height[right]:
                area = height[left] * (right-left)
                left = left+1
            else:
                area = height[right] * (right-left)
                right = right-1
            if area>max_area:
                max_area = area
        return max_area