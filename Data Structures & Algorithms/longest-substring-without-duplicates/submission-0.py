class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = {}
        maximum = 0
        i = 0
        start = 0

        while i < len(s):
            if s[i] in idx and idx[s[i]] >= start:
                start = idx[s[i]] + 1

            idx[s[i]] = i
            maximum = max(maximum, i - start + 1)
            i += 1

        return maximum     