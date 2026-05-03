class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        total = 0
        for pile in piles:
            total += pile

        low = 1
        high = total - (len(piles) - 1)
        k = 0
        while low <= high:
            m = (low + high) // 2
            if self.guess(m, h, piles) > 0:
                high = m - 1
                k = m
            elif self.guess(m, h, piles) < 0:
                low = m + 1
            
 
        return k
        

    def guess(self, m, h, piles):
        hours = 0
        for pile in piles:
            hours += (pile + m - 1) // m

        if hours > h:
            return -1
        elif hours <= h:
            return 1
