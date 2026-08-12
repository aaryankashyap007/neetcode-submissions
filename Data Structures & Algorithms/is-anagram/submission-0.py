class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l1 = list(s)
        l2 = list(t)

        l1.sort()
        l2.sort()

        for n in range(len(l1)):
            if l1[n] != l2[n]:
                return False
        
        return True