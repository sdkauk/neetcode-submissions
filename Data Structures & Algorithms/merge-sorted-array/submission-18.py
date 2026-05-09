class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        j = m - 1
        k = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if k >= 0:
                if nums1[j] >= nums2[k] and j >= 0:
                    nums1[i] = nums1[j]
                    j -= 1
                else:
                    nums1[i] = nums2[k]
                    k -= 1



        j = 0
        k = -1
        i = 1

        [1,2,2,3,5,6]
        [2,5,6]