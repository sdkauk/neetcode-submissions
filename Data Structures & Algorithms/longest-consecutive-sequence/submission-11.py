class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 1
        for num in numSet:
            if num - 1 not in numSet:
                streak = 1
                while num + streak in numSet:
                    streak += 1
                    longest = max(longest, streak)

        if not numSet:
            return 0

        return longest


