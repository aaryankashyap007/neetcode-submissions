class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        prefix = str2[:len(str1)]
        suffix = str2[-len(str1):]
        return str1 == prefix and str1 == suffix

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range (len(words) - 1):
            for j in range (i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans