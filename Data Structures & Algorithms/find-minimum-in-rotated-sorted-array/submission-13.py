class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]
    
        low = 0
        high = len(nums) - 1
        n = len(nums)

        minval = self.binarySearch(low, high, nums)
        return minval

    def binarySearch(self, low, high, nums):

        if low >= high:
            return -1

        while low < high:
            m = (low + high) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m] < nums[m - 1]:
                return nums[m]
            
            right = self.binarySearch(m + 1, high, nums)
            if right != -1:
                return right
            
            left = self.binarySearch(low, m - 1, nums)
            if left != -1:
                return left

            return -1


        # while low < high:
        #     m = (low + high) // 2
        #     i = m - n
        #     if nums[i] < nums[i + 1] or nums[i] < nums[i - 1]:
        #         return nums[i + 1] 

        #     elif nums 