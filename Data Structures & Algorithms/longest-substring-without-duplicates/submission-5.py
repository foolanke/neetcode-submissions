class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        best = 0
        seen = set()

        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = right - left + 1
            if length > best:
                best = length
            right += 1
        
        return best