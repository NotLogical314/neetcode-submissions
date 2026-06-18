class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max = deque()
        output = []
        l = r = 0

        while r < len(nums):
            while max and nums[max[-1]] < nums[r]:
                max.pop()
            max.append(r)

            if l > max[0]:
                max.popleft()

            if (r+1) >= k:
                output.append(nums[max[0]])
                l += 1
            r += 1

        return output