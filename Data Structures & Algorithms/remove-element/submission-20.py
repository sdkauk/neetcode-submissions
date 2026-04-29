class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        L = 0
        for R in range(len(nums)):
            if nums[R] == val:
                R += 1
            else:
                nums[L] = nums[R]
                L += 1
                R += 1
        return L