class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        left = 0
        ans = 1

        for right in range(1, n):
            cmp = (arr[right - 1] > arr[right]) - (arr[right - 1] < arr[right])

            if cmp == 0:
                left = right
            elif right == n - 1 or cmp * (
                (arr[right] > arr[right + 1]) - (arr[right] < arr[right + 1])
            ) != -1:
                ans = max(ans, right - left + 1)
                left = right

        return ans