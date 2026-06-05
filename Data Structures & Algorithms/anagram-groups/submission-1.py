class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        
        for word in strs:
            new = "".join(sorted(word))
            if new not in dct:
                dct[new] = []
                
            dct[new].append(word)

        return list(dct.values())