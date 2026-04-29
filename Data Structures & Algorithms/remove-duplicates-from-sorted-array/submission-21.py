class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums [r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l


#             L
#[1,2,4,6,7,8,7,8,7,7,8]
#                 R