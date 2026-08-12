class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        return sorted(a) == sorted(b)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list = []
        x = len(strs)
        done = [0] * x
        for n in range(x):
            if done[n] == 0:
                lst = []
                lst.append(strs[n])
                for m in range(n + 1, x):
                    if self.isAnagram(strs[m], strs[n]):
                        lst.append(strs[m])
                        done[m] += 1
                anagrams_list.append(lst)
        return anagrams_list