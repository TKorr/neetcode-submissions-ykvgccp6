class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # char -> index (last)
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                # max(left, lastIndex[char] + 1)
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res