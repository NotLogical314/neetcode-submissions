class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for _ in s:
            if _ in count:
                count[_] += 1
            else:
                count[_] = 1

        for _ in t:
            if _ in count:
                count[_] -= 1
            else:
                return False

        return all(value == 0 for value in count.values())