class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = [[nums[i], i] for i in range(len(nums))]
        nums_index.sort()
        x, y = 0, len(nums_index) - 1
        while x < y:
            curr = nums_index[x][0] + nums_index[y][0]
            if target == curr:
                return sorted([nums_index[x][1], nums_index[y][1]])
            elif target < curr:
                y -= 1
            else:
                x += 1
