class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            # if char in current substring char set
            # move window right and remove s[left] from char set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            # max length from length of window
            max_len = max(max_len, right - left + 1)
        
        return max_len
