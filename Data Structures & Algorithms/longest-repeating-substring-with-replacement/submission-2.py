class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        left = 0
        best = 0

        for right in range(len(s)):
            d[s[right]] += 1

            while (right - left + 1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
            right += 1

        return best