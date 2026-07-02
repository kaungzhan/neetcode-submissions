class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = water_trapped_at_i = total_water = 0
        l,r = 0, len(height) - 1 
        while l < r:
            if height[l] <= height[r]:
                max_left = max(max_left, height[l])
                water_trapped_at_i = max_left - height[l]
                total_water += water_trapped_at_i
                l += 1
            else:
                max_right = max(max_right, height[r])
                water_trapped_at_i = max_right - height[r]
                total_water += water_trapped_at_i
                r -= 1
        return total_water