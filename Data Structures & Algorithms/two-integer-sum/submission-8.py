class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = defaultdict(int)

        for i, num in enumerate(nums):
            need = target - num

            if need in mydict:
                return [mydict[need],i]

            mydict[num] = i