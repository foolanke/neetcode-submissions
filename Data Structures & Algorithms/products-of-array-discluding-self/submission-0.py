class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            prod = 1
            for j, k in enumerate(nums): 
                if i == j:
                    continue
                prod = prod * k
            result.append(prod)
        return result



#for each element in the list, compute the product of all the other values
# to do that, loop through it again keeping a product tracker


            