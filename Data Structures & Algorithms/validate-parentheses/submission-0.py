class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in matching:
                if stack and matching[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False