class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        countS1, countS2 = {}, {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)
        l = 0
        size = len(s1)
        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)
            if r - l + 1 > size:
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1
            if countS1 == countS2:
                return True 
        return False
                 

