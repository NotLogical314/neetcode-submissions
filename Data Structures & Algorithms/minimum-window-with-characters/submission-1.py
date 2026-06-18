class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for char in  t:
            need[char] = need.get(char , 0) + 1
        
        needed = len(need)
        formed = 0
        start = 0
        left = 0
        min_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch , 0) + 1

            if ch in need and need[ch] == window[ch]:
                formed += 1

            while formed == needed:
                if right - left + 1 < min_len:
                    min_len = min(min_len , right - left + 1)
                    start = left

                window[s[left]] -= 1

                if s[left] in need and need[s[left]] > window[s[left]]:
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ''

        return s[start:start + min_len]