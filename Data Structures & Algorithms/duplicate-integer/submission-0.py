class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        return any(count>1 for count in nums_count.values())
