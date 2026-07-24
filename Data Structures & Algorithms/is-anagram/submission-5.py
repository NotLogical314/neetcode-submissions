class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictio = defaultdict(int)

        for word in s:
            dictio[word] += 1

        for word in t:
            if word in dictio:
                dictio[word] -= 1


        for value in dictio.values():
            if value != 0:
                return False
        return True