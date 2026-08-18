class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in groups:
                groups[sortedS] = []
            groups[sortedS].append(s)
        return list(groups.values())