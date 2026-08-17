class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = []
        right = []
        result = []
        multiplier = 1
        for i in range(n):
            left.append(multiplier)
            multiplier *= nums[i]
        multiplier = 1
        for i in range(n - 1, -1, -1):
            right.append(multiplier)
            multiplier *= nums[i]
        right.reverse()
        for i in range(n):
            result.append(left[i] * right[i])
        return result
            



#for each element in the list, compute the product of all the other values
# to do that, loop through it again keeping a product tracker


            