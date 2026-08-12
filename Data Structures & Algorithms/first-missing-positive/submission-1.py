class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        arr = [0] * n
        for i in range(n):  
            if nums[i] > 0 and nums[i] <= n:
                arr[nums[i] - 1] = -1
        for i in range(n):
            if arr[i] != -1:
                return i + 1
        return n + 1