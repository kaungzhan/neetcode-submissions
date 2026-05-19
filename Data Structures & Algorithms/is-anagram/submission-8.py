class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False 
      countS, countT = {}, {}
      for word in s:
        countS[word] = 1 + countS.get(word, 0)
      for word in t:
        countT[word] = 1 + countT.get(word, 0)
      for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
      return True 
