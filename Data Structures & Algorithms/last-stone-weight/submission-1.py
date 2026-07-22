class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if first == second:
                continue 
            else:
                heapq.heappush_max(stones, first-second)
        
        return  heapq.heappop_max(stones) if stones else 0