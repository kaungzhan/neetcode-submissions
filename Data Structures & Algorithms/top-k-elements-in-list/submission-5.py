import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        top_k = counter.most_common(k)
        return [x for x, _ in top_k]