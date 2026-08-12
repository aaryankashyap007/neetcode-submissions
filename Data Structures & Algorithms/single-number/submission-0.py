class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if num not in ans:
                ans.append(num)
            else:
                ans.remove(num)
        return ans[0]