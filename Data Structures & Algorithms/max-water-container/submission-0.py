class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        curr_area = 0

        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            area = max(curr_area, area)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right -= 1

        return area