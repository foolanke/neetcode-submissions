class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)

        left = 0
        n = len(s)
        maxlen = 0

        for right in range(n): 
            length = right - left + 1
            counts[s[right]] += 1
            while length - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
                length -= 1
            if length > maxlen:
                maxlen = length
        
        return maxlen