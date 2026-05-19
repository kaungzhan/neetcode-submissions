import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in collections.Counter(nums).most_common(k)]