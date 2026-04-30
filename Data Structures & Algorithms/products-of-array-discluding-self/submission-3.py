class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = []
        suffix = [1] * n
        output = []

        pre = 1
        for num in nums:
            pre = pre * num
            prefix.append(pre)

        suf = 1
        for i in range(len(nums) -1, -1, -1):
            suf = suf * nums[i]
            suffix[i] = suf

        for i in range(len(prefix)):
            if i == 0:
                output.append(1 * suffix[i +1])

            elif i == n -1:
                output.append(prefix[i-1] * 1)

            else:
                output.append(prefix[i -1] * suffix[i + 1])

        return output

