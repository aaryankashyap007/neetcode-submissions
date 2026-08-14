class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = n, n
        for idx in range(n):
            if nums[idx] == 0:
                i = idx
                break
        if i < n:
            for idx in range(i, n):
                if nums[idx] != 0:
                    j = idx
                    break
            while i < n and j < n:
                if nums[i] != 0:
                    i += 1
                    continue
                if nums[j] == 0:
                    j += 1
                    continue
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
