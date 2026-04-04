bracket_map = {
    "}": "{",
    ")": "(",
    "]": "[",
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if len(stack) == 0 or stack.pop() != bracket_map[char]:
                    return False
        return len(stack) == 0