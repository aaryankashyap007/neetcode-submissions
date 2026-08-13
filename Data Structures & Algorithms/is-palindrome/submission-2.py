class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        if not s:
            return True
        n = len(s)
        for i in range(n // 2 + 1):
            if s[i] != s[n - i - 1]:
                return False
        return True