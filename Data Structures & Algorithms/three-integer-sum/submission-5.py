class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            front = i + 1
            back = n - 1
            target = -nums[i]
            while front < back:
                curr = nums[front] + nums[back]
                if curr < target:
                    front += 1
                elif curr > target:
                    back -= 1
                else: 
                    res.append([nums[front], nums[back], nums[i]])
                    front += 1
                    back -= 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
        
        return res