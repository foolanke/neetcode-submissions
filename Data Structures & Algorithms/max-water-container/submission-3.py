class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            if heights[left] < heights[right]: 
                most = max(most, heights[left] * (right - left))
                left += 1
            else:
                most = max(most, heights[right] * (right - left))
                right -= 1
            
        return most
