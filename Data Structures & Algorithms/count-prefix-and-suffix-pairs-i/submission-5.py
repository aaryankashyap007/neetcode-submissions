class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and  str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range (len(words) - 1):
            for j in range (i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans