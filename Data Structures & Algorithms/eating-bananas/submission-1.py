class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1 #13
        high = 0 #25

        for pile in piles:
            high = max(high, pile)
        
        rate = 0 #2
        while low <= high:
            m = (low + high) // 2
            if self.check(piles, m) > h:
                low = m + 1

            elif self.check(piles, m) <= h:
                rate = m
                high = m - 1

        return rate
    
    def check(self, piles, val):
        totalHours = 0 # 4
        for pile in piles:
            h = (pile + val - 1) // val
            totalHours += h

        return totalHours
        
