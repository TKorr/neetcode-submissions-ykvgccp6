class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.integer_stream = nums
        

    def add(self, val: int) -> int:
        self.integer_stream.append(val)

        # sort stream and output self.integer_stream[k]
        sorted_stream = sorted(self.integer_stream, reverse=True)
        print(sorted_stream)
        return sorted_stream[self.k - 1]
        
