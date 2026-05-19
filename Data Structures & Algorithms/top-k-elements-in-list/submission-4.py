class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       result = [item for items, c in Counter(nums).most_common() for item in [items] * c]
       new_result = []
       [new_result.append(val) for val in result if val not in new_result]
       frequency = []
       for i in range(k):
        frequency.append(new_result[i])
       return frequency
        
        