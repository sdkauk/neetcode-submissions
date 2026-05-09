class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0
        for num in numset:
            streak = 1
            if num - streak not in numset:
                while num + streak in numset:
                    streak += 1
                longest = max(streak, longest)
        
        return longest