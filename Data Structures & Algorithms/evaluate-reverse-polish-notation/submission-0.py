class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t == "+":
                b = nums.pop()
                a = nums.pop()
                ans = a + b
                nums.append(ans)
            elif t == "-":
                b = nums.pop()
                a = nums.pop()
                ans = a - b
                nums.append(ans)
            elif t == "*":
                b = nums.pop()
                a = nums.pop()
                ans = a * b
                nums.append(ans)
            elif t == "/":
                b = nums.pop()
                a = nums.pop()
                ans = int(a/b)
                nums.append(ans)
            else:
                nums.append(int(t))
        
        return nums[0]