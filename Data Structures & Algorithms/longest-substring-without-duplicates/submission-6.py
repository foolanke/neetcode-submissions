class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        best = 0
        seen = set()

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            length = right - left + 1
            if length > best:
                best = length
        
        return best