class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans1 = [1] * n
        ans2 = [1] * n
        ans = [1] * n
        for i in range(n - 1):
            ans1[i + 1] = ans1[i] * nums[i]
        for i in range (n - 1, 0, -1):
            ans2[i - 1] = ans2[i] * nums[i]
        for i in range(n):
            ans[i] = ans1[i] * ans2[i]
        return ans