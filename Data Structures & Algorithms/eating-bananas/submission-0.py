class Solution:

    def hours(self, piles: List[int], rate: int) -> int:
        count = 0
        for pile in piles:
            hours_for_pile = (pile + rate - 1) // rate
            count = count + hours_for_pile
        return count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            if self.hours(piles, mid) > h:
                low = mid + 1
            else:
                high = mid
        
        return low