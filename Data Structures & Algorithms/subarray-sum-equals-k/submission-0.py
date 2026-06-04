class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        count = 0
        ini = 0

        for num in nums:
            ini += num

            count += prefix.get(ini-k , 0)

            prefix[ini] = prefix.get(ini,0) + 1

        return count 