import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k upper bound = max(piles)
        # k lower bound = 1

        r = max(piles)
        l = 1
        while l <= r:
            m = l + (r - l) // 2
            if self.totalEatingHours(piles, m) > h:
                l = m + 1
            elif self.totalEatingHours(piles, m) <= h:
                r = m - 1
            else:
                break
        return l

    def totalEatingHours(self, piles: int, k: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours