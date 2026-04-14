class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # +1 for 0 freq


        '''
        {
            1:2,
            2:1,
            3:3,
            4:3
        }
        '''
        for num in nums:
            count[num] = 1 + count.get(num,0)

        '''
        {
            [],
            [2],
            [1],
            [3,4]
        }
        '''
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        


