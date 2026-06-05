class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        
        for word in strs:
            lst = [0] * 26
            for _ in word:
                lst[ord(_) - ord('a')] += 1
            dct[tuple(lst)].append(word)

        return list(dct.values())