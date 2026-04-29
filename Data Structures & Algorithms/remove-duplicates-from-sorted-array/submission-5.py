class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 1
        for f in range(1, len(nums)):
            if nums[f] != nums[f-1]:
                nums[s] = nums[f]
                s += 1

        return s


        #    S
        # [1,2,2,3,4]
        #        F 

        #CHALLENGE: make it work with f = 0, or figure out if it can work