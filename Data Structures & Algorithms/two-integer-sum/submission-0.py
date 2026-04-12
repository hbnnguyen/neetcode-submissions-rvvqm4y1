class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, num in enumerate(nums):
            difference = (target - num)

            if difference in differences:
                return [min(i, differences[difference]), max(i, differences[difference])]
            else:
                differences[num] = i