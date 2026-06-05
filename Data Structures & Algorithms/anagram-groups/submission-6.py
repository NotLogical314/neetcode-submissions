class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        
        for word in strs:
            lst = [0] * 26

            for _ in word:
                lst[ord(_) - ord('a')] += 1
            key = tuple(lst)

            if key not in dct:
                dct[key] = []

            dct[key].append(word)

        return list(dct.values())