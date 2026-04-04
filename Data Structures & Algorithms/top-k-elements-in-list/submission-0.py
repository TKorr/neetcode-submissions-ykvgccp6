from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # single parse build frequency dict where key is count and value is element

        cnt = Counter()

        for num in nums:
            cnt[num] += 1

        k_most_common = cnt.most_common(k)

        result = [i for i, j in k_most_common]
        return result
