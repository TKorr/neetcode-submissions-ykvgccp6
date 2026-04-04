import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # count number of unique tasks 
        count = Counter(tasks)
        
        # store negative counts in heap
        # Python only uses min heaps, so need to store negatives to emulate a max heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # for each task on heap, pop largest value to process, and reduce by 1, push back onto heap
        # if task value == 0, do not push to queue or heap
        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        # while maxHeap or q not empty
        while maxHeap or q:
            # increase time by 1
            time += 1

            # if maxHeap is not empty process item
            if maxHeap:
                # if maxHeap is not empty, pop value, add 1
                cnt = 1 + heapq.heappop(maxHeap)
                # if cnt is not zero append to q with time + n delay
                if cnt:
                    q.append([cnt, time + n])

            # if q is not empty and current top item is at time, pop item off q onto heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
