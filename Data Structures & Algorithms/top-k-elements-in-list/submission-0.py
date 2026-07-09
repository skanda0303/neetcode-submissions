class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        heap = []
        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
        res = []
        while k>0:
            key,value = heapq.heappop(heap)
            res.append(value)
            k-=1
        return res
