class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            freq[i] += 1

        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        