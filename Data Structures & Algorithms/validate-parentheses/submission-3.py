class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '[':']',
            '(':')',
            '{':'}'
        }
        stack = []

        for _ in s:
            if _ in match:
                stack.append(_)
            else:
                if not stack or  _ != match[stack[-1]]:
                    return False
                stack.pop()

        return  len(stack) == 0
