class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in hash1:
                hash1[key].append(s)
            else:
                hash1[key] = [s]

        return list(hash1.values())