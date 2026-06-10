class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for ch in s:
            if ch in d:
                if not stack or stack[-1] != d[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
            