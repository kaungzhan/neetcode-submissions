class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       result = [items for items,_ in Counter(nums).most_common() ]
       #new_result = []
       #[new_result.append(val) for val in result if val not in new_result]
       frequency = []
       for i in range(k):
        frequency.append(result[i])
       return frequency
        
        