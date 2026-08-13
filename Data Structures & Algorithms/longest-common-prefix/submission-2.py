class Solution:
    def prefix(self, a: str, b: str) -> str:
        if a == "" or b == "":
            return ""
        i = 0
        pre = []
        lst1, lst2 = list(a), list(b)
        while i < len(a) and i < len(b):
            if lst1[i] != lst2[i]:
                break
            pre.append(lst1[i])
            i += 1
        return "".join(pre)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = self.prefix(strs[i], ans)
            if ans == "":
                break
        return ans