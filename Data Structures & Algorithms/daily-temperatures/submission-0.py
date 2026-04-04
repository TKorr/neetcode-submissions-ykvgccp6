class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in temperatures]

        for i, temperature in enumerate(temperatures):

            while stack and temperature > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j

            stack.append(i)

        return result

