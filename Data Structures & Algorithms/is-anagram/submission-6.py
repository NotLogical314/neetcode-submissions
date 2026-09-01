class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = defaultdict(int)

        for _  in s:
            if _.isalpha():
                mydict[_] += 1

        for _ in t:
            if _.isalpha():
                mydict[_] -= 1

        for _ in mydict.values():
            if _ != 0:
                return False
        return True