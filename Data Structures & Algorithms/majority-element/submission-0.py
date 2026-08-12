class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        curr = nums[0]
        for num in nums:
            if curr != num:
                count = 1
                curr = num
            else:
                count += 1
                if count > n/2:
                    return curr