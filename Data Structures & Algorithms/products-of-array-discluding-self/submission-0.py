class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
        
        if len(zeroes) > 1:
            return [0] * len(nums)
        elif len(zeroes) == 1:
            arr = [0] * len(nums)
            prod = 1
            for num in nums:
                if num != 0:
                    prod = prod * num
            arr[zeroes[0]] = prod
            return arr
        else:
            prod = 1
            for num in nums:
                prod = prod * num
            
            arr = []
            for num in nums:
                arr.append(int(prod/num))
            
            return arr