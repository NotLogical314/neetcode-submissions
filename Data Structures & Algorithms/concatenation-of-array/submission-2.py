class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2* len(nums)
        for _ in range(len(nums)):
            ans[_] = nums[_]
            ans[_+len(nums)]= nums[_] 

        return ans