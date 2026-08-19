class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            target = -nums[i]
            front = i + 1
            back = n - 1

            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            while front < back:
                if nums[front] + nums[back] == target:
                    ans.append([nums[i], nums[front], nums[back]])
                    front += 1
                    back -= 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
                elif nums[front] + nums[back] > target:
                    back -= 1
                else:
                    front += 1
        return ans