class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            counts = [0] * 26

            for c in i:
                counts[ord(c) - ord('a')] += 1
            res[tuple(counts)].append(i)
        return list(res.values())
        