class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        output = []
        for i in range(len(nums)):
            output.append(pre)
            pre = nums[i] * pre
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * post
            post = post * nums[i]

        return output

