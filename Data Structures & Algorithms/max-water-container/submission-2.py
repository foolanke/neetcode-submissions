class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        greatest = 0
        right = n - 1
        left = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            if width * height > greatest:
                greatest = width * height
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return greatest