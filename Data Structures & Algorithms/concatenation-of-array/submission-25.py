class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0] * (n * 2)
        for i, num in enumerate(nums):
            output[i] = output[i + n] = num
        return output