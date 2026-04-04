class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        

        def backtrack(start, path):
            result.append(path[:])   # ← record current subset

            for i in range(start, len(nums)):

                path.append(nums[i])       # ← choose
                backtrack(i + 1, path)     # ← explore
                path.pop()                 # ← undo (backtrack)

        backtrack(0, path)
        return result
