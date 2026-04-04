class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        st = Counter(t)

        return sc == st
