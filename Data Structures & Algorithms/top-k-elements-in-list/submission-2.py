import heapq
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for num in frequencies:
            heapq.heappush(pq, (-frequencies[num], num))

        for i in range(0, k):
            res.append(heapq.heappop(pq)[1])
        
        return res
        
            

            
            





        