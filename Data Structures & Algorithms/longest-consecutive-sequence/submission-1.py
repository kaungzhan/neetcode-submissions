class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       my_nums = set(nums)
       longest = 0
       for n in nums:
        if (n-1) not in my_nums:
            r = 0
            while (n + r) in my_nums:
                r += 1
            longest = max(r, longest)
       return longest 
