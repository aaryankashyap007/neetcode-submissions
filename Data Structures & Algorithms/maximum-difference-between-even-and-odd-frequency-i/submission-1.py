from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        s_freq = Counter(s)
        odd = []
        even = []
        for num in s_freq.values():
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return max(odd) - min(even)