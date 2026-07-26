class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = [0] * l
        stack = []
        for i in range(l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                p = stack.pop()
                result[p] = i - p
            stack.append(i)
        while stack:
            result[stack.pop()] = 0
        return result