from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left != right:
            currentSum = numbers[left] + numbers[right]

            if currentSum == target:
                return [left + 1, right + 1]

            if currentSum > target:
                right -= 1
            else:
                left += 1

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1,0], -1))