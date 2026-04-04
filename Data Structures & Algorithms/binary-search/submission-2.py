class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums:
            return -1
        
        def bin_search(l,r):
            if l > r:
                return -1

            mid = (l + r) // 2

            if nums[mid] < target:
                return bin_search(mid + 1, r)
            
            if nums[mid] > target:
                return bin_search(l, mid - 1)
            
            if nums[mid] == target:
                return mid

        return bin_search(0,n-1)