class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0] * (n * 2)
        for i in range(n):
            output[i-1] = nums[i-1]

        for i in range(n):
            output[(i-1) + n] = nums[i-1]

        return output