class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        n = len(numbers)
        front = 0
        back = n - 1
        while front < back:
            sum = numbers[front] + numbers[back]
            if sum == target:
                ans.append(front + 1)
                ans.append(back + 1) 
                return ans
            elif sum < target:
                front += 1
                continue
            else:
                back -= 1
                continue