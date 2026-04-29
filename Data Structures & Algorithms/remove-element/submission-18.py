class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1

        return l

#         L
#[1,3,5,3,2,3,5,3] val = 2
#           R