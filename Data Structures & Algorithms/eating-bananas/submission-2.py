class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1 calculate the range we are searching
        # Step 2 Do a binary search range and check

        l = 1
        high = max(piles)
        k = 0

        while l <= high:
            m = (l + high) // 2

            if self.check(piles, m) > h:
                l = m + 1
            elif self.check(piles, m) <= h:
                k = m
                high = m - 1

        return k

    
    def check(self, piles, m):

        r = 0
        for pile in piles:
            r += (pile + m - 1) // m
        
        return r
