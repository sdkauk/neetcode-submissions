class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        L = 0
        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1
        return L

#       L          L
#[1,3,3,5,5,3,5,3] val = 2
#         R              R