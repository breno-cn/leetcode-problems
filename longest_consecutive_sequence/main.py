from typing import List

import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        heapq.heapify(nums)

        sequenceLength = 1
        biggestSequence = 1

        current = heapq.heappop(nums)
        while len(nums) > 0:

            difference = nums[0] - current
            if difference == 1:
                sequenceLength += 1
            elif difference != 0:
                if sequenceLength > biggestSequence:
                    biggestSequence = sequenceLength
                sequenceLength = 1

            current = heapq.heappop(nums)

        return max(sequenceLength, biggestSequence)
    

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))                       # 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))                   # 9
print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))               # 7
print(solution.longestConsecutive([1,2,0,1]))                               # 3
