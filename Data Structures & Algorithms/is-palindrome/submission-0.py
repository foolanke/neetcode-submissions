class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        front = 0
        back = n - 1
        while front < back:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue
            if s[front].lower() == s[back].lower():
                front += 1
                back -= 1
            else:
                return False
        return True