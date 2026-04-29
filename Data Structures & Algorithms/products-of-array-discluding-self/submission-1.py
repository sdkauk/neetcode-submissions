class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        index1 = 0
        index2 = 0
        for j in nums:
            i = 1
            index1 += 1
            for k in nums:
                index2 += 1
                if (index1 != index2):
                    i = i*k
            index2 = 0
            output.append(i)
            i = None;
    
        return output
