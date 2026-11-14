class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        res = []

        for i in nums:
            freq[i] += 1
        
        sortedlist = sorted(freq, key=freq.get, reverse=True)
        for i in sortedlist:
            res.append(i)
            if (len(res)) == k:
                return res