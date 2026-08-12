class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = [0, 0, 0]
        for num in nums:
            colours[num] += 1
        
        i = 0
        for _ in range(colours[0]):
            nums[i] = 0
            i += 1
        
        for _ in range(colours[1]):
            nums[i] = 1
            i += 1
        
        for _ in range(colours[2]):
            nums[i] = 2
            i += 1