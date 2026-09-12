class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        windowsize = len(s1)
        fingerprint = [0] * 26
        matching = [0] * 26

        left = 0
        right = left + windowsize

        # build the first window
        for i in range(left, right):
            fingerprint[ord(s1[i]) - ord('a')] += 1
            matching[ord(s2[i]) - ord('a')] += 1

        if fingerprint == matching:
            return True

        while right < len(s2):
            matching[ord(s2[right]) - ord('a')] += 1   # right enters
            matching[ord(s2[left]) - ord('a')] -= 1    # left leaves
            right += 1
            left += 1
            if fingerprint == matching:
                return True

        return False