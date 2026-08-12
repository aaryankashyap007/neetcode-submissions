class Solution:
    def similar(self, s1: str, s2: str) -> bool:
        lst1 = list(s1)
        lst1.sort()
        lst2 = list(s2)
        lst2.sort()
        return lst1 == lst2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        while j <= len(s2):
            slice = s2[i:j]
            if self.similar(slice, s1):
                return True
            i += 1
            j += 1
        return False