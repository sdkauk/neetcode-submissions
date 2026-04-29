class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        allNums = set()

        for num in nums:
            if num in allNums:
                return True
            else:
                allNums.add(num)

        return False