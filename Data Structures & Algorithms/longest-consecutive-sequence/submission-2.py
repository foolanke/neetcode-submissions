class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxlen = 0
        for n in numset:
            length = 0
            temp = n
            if (n - 1) in numset:
                continue
            while (temp) in numset:
                length += 1
                temp += 1
            if length > maxlen:
                maxlen = length
        
        return maxlen