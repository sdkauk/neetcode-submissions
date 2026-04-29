class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        most = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current > most:
                    most = current
            else:
                current = 0
        
        return most
            