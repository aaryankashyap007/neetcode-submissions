class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        curr = 1
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr += 1
            else:
                if curr > streak:
                    streak = curr
                curr = 1
        
        if curr > streak:
            streak = curr
        
        return streak