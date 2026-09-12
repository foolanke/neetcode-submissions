class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streak = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            streak = max(streak, right - left + 1)

        return streak