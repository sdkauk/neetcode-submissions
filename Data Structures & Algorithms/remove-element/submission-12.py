class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            L = 0
            for R in range(len(nums)):
                if nums[R] != val:
                    nums[L] = nums[R]
                    L += 1

            return L
                    

#       L
#[1,3,5,2,4,2,5,3] val = 2
#         R