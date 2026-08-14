class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        nums1[:] = nums1[:m]
        if not nums1:
            nums1.extend(nums2)
            return
        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
        while j < n:
            nums1.append(nums2[j])
            j += 1