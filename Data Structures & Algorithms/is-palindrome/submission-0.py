class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = s.replace(" ", "").lower()
        clean_string = ''.join([char for char in clean_string if char.isalnum()])
        print(clean_string)
        left = 0
        right = len(clean_string) - 1

        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
