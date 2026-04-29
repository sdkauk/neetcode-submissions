class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1 

        return L
#       L   
#[1,3,3,3,5,3]
#         R

#[1,3,2,3,5,5]