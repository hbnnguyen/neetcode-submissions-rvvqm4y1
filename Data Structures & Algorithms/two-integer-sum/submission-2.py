class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, num in enumerate(nums):
            difference = (target - num)

            if difference in prev:
                return [min(i, prev[difference]), max(i, prev[difference])]
            else:
                prev[num] = i