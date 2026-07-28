class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, o, c) :
            #base case 
            if len(path) == 2 * n:
                res.append(path)
                return 
            if o < n:
                backtrack(path + "(", o + 1, c)
            if c < o:
                backtrack(path + ")", o , c + 1)
        backtrack("", 0, 0)
        return res