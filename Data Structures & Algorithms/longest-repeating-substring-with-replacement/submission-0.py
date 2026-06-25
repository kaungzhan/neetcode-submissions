class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        num_replacement, result = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            num_replacement = r - l + 1 - max(freq.values()) 
            if num_replacement > k:
                freq[s[l]] -= 1
                l += 1 
            result = max(result, r - l + 1)
        return result