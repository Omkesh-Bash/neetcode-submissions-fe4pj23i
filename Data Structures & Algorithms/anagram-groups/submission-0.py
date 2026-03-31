class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str in strs:
            alp = [0]*26
            for c in str:
                alp[ord(c) - ord('a')] += 1
            group[tuple(alp)].append(str)
        return list(group.values())