from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numbers = set(nums)
        biggestSequence = 1

        for num in numbers:    
            sequenceLength = 1
            previous = num - 1
            
            if previous in numbers:
                continue

            currentNumber = num + 1
            while currentNumber in numbers:
                sequenceLength += 1
                currentNumber += 1

            if sequenceLength > biggestSequence:
                biggestSequence = sequenceLength
        
        return max(biggestSequence, sequenceLength)
    

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))                       # 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))                   # 9
print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))               # 7
print(solution.longestConsecutive([1,2,0,1]))                               # 3
