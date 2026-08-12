class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        ans = []
        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])
        
        ans.append(word1[n:])
        ans.append(word2[n:])
        return ''.join(ans)