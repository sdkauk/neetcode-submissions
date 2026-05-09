class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        last = m + n - 1
        j = m - 1
        k = n - 1

        while k >= 0:
            if nums1[j] >= nums2[k] and j >= 0:
                nums1[last] = nums1[j]
                j -= 1
            else:
                nums1[last] = nums2[k]
                k -= 1

            last -= 1