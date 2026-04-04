class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:

            ans = numbers[left_pointer] + numbers[right_pointer]
            if ans > target:
                right_pointer -= 1

            if ans < target:
                left_pointer += 1
            
            if ans == target:
                return [left_pointer + 1, right_pointer + 1]

