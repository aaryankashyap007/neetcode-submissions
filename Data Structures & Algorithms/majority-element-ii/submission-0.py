class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lim = n // 3

        nums.sort()

        curr = 1
        ans = []
        for i in range(1, n):
            if curr > lim:
                ans.append(nums[i - 1])

            if nums[i] == nums[i - 1]:
                curr += 1
            else:
                curr = 1
        
        if curr > lim:
            ans.append(nums[n - 1])

        return list(set(ans))