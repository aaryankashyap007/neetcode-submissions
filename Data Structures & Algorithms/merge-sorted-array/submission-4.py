class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        # nums1[:] = nums1[:m]
        # if not nums1:
        #     nums1.extend(nums2)
        #     return
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] == nums2[j]:
        #         nums1.insert(i, nums2[j])
        #         i += 1
        #         j += 1
        #     else:
        #         nums1.insert(i, nums2[j])
        #         j += 1
        # while j < n:
        #     nums1.append(nums2[j])
        #     j += 1
        temp = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                temp.append(nums1[i])
                temp.append(nums2[j])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        if j < n:
            while j < n:
                temp.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                temp.append(nums1[i])
                i += 1
        nums1[:] = nums1[:0]
        nums1.extend(temp)