class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)

        count = []
        startSequence = False

        for num in nums:
            seqCount = 0

            if num - 1 not in numSet:
                startSequence = True
                seqCount += 1

            i = num + 1
            while startSequence:
                if i in numSet:
                    seqCount += 1
                    i += 1
                else:
                    startSequence = False
                    count.append(seqCount)

        return max(count)

