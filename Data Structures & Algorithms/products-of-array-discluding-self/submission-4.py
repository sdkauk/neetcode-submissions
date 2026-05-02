class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        pre = 1
        for i, num in enumerate(nums):
            output.append(pre)
            pre = pre * num

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * post
            post = post * nums[i]
        
        return output

