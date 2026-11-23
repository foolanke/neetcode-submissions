class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        key = defaultdict(int)
        compare = defaultdict(int)

        for c in s1: 
            key[c] += 1
        
        left = 0
        for right in range(len(s2)):
            compare[s2[right]] += 1

            while (right - left + 1) > len(s1):
                compare[s2[left]] -= 1
                if compare[s2[left]] == 0:
                    del compare[s2[left]]
                left += 1
                
            if key == compare:
                return True
        
        return False