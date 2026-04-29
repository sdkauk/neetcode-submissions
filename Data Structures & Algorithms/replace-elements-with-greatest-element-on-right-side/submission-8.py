class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new = [0] * len(arr)
        highest = -1

        for i in range(len(arr) - 1, -1, -1):
            new[i] = highest
            highest = max(highest, arr[i])
        return new
            

            
            