class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, path):
            #base case 
            if sum(path) == target:
                res.append(path[:])
                return 
            if idx>=len(nums) or sum(path) > target:
                return 
            path.append(nums[idx])
            backtrack(idx, path)
            path.pop()
            backtrack(idx+1, path)

        backtrack(0,[])
        return res
            