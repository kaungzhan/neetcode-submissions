class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, runningSum = nums[0], nums[0]
        for n in nums[1:]:
            runningSum = max(n, n + runningSum)
            maxSum = max(runningSum,maxSum)
        return maxSum
