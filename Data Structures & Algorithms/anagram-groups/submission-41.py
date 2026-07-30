class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for str in strs:
            counter = [0]*26
            for c in str:
                counter[ord(c) - ord("a")] += 1
            lookup(tuple(counter)).append(str)
        
        return list(lookup.items())