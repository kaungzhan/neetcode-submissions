class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        mapping = {'2' : ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4':['g', 'h', 'i'],
        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z'] }
        def backtrack(idx, string):
            if idx == len(digits):
                res.append(string)
                return 
            letters = mapping[digits[idx]]
            for l in letters:
                new_string = string + l
                backtrack(idx+1, new_string)
        backtrack(0, "")
        return res
            