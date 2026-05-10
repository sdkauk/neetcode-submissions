class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        k = 0

        while low <= high:
            m = (low + high) // 2
            if self.check(piles, m) > h:
                low = m + 1
            elif self.check(piles, m) <= h:
                k = m
                high = m - 1
            
        return k

    def check(self, piles, m):
        h = 0
        for pile in piles:
            h += (pile + m - 1) // m
        
        return h