class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        front = 0
        back = n - 1

        while front < back:
            curr = numbers[front] + numbers[back]
            if curr > target:
                back -= 1
            elif curr < target:
                front += 1
            elif curr == target:
                return [front + 1, back + 1]
            