class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        for i in range(len(nums)):
            if nums[i] not in idx:
                idx[nums[i]] = [i]
            else:
                for num in idx[nums[i]]:
                    if abs(num - i) <= k:
                        return True
                idx[nums[i]].append(i)
        return False