class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            fp = defaultdict(int)
            for c in str:
                    fp[c] += 1

            result[tuple(fp)].append(str)

        return list(result.values)