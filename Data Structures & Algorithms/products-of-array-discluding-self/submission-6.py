class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        output = []
        for num in nums:
            output.append(pre)
            pre *= num
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = post * output[i]
            post *= nums[i]

        return output
            
