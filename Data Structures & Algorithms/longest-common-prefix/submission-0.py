class Solution:
    def prefix(self, a: str, b: str) -> str:
        l1 = list(a)
        l2 = list(b)
        chars = []

        min = 0
        if len(a) < len (b):
            min = len(a)
        else:
            min = len(b)
        
        for n in range(min):
            if a[n] != b[n]:
                break
            chars.append(a[n])
        
        return ''.join(chars)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for string in strs:
            result = self.prefix(result, string)
        
        return result