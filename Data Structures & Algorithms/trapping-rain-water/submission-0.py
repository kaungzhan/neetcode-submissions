class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = maxRight = water_trapped_at_i = total_water = 0
        for i in range(1, len(height) - 1):
            maxLeft = max(maxLeft, height[i - 1])
            maxRight = 0
            for j in range(i + 1, len(height)):
                maxRight = max(maxRight, height[j])
            water_trapped_at_i = max(0, min(maxLeft, maxRight) - height[i])
            total_water += water_trapped_at_i
        return total_water