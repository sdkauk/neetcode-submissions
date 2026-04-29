class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0] * (n * 2)
        for i in range(n):
            output[i] = nums[i]
            output[i + n] = nums[i]

        return output