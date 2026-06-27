class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)

        final = []

        for i in nums: 
            count[i] += 1
        
        for x in range(k):
            target = max(count, key=count.get)
            final.append(target)
            del count[target]

        return final