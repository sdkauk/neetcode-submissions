class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove duplicates
        # return number of unique elments (length of the array)

        pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer - 1]:
                nums[pointer] = nums[i]
                pointer += 1

        return pointer

