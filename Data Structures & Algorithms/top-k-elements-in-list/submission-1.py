class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            count[num] += 1

        for i, n in count.items():
            freq[n].append(i)

        res = []
        for j in range(len(freq) -1, 0, -1):
            for x in freq[j]:
                res.append(x)
                if len(res) == k:
                    return res
