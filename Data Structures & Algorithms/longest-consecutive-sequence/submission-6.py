class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        longest = 1
        last = nums[0]
        streak = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            
            elif nums[i] == last:
                continue
            
            elif nums[i] == last + 1:
                streak += 1
            
            else:
                streak = 1
            if streak > longest:
                longest= streak
            last = nums[i]
        return longest
