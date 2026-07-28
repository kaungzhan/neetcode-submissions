class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palidrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1 
            return True 

        def backtrack(start, temp):
            if start == len(s):
                res.append(temp.copy())
                return 
            for end in range(start, len(s)):
                if is_palidrome(s, start, end):
                    temp.append(s[start:end+1])
                    backtrack(end+1, temp)
                    temp.pop()
        backtrack(0, [])
        return res
            