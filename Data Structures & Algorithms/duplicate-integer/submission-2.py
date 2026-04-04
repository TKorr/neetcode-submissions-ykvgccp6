class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        counts = Counter(nums)

        most_common = counts.most_common(1)

        if most_common[0][1] > 1:
            return True
        return False

        