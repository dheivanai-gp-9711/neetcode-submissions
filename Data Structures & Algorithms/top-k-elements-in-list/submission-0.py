import heapq
from collections import Counter
class Solution:#infact this is my google qn
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        hey=Counter(nums)
        print(hey)
        for key, value in hey.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        li=[]
        print(heap)
        for a,b in heap:
            li.append(b)
        return li
