class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for str in strs:
            fp = [0]*26
            for char in str:
                fp[ord(char) - ord('a')] += 1
            result[tuple(fp)].append(str)

        return list(result.values())