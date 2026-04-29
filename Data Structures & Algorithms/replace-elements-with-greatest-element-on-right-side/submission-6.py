class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new = [0] * len(arr)
        highest = 0

        if len(arr) == 1:
            return [-1]
        for i in range(1, len(arr)):
            if -i == -1:
                highest = arr[-i]
                new[-1] = -1
                continue
            new[-i] = highest
            if arr[-i] > highest:
                highest = arr[-i]

        new[0] = highest
        return new
            

            
            