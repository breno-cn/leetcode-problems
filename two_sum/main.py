from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing_to_target = [0] * len(nums)
        missing_to_target_pos = dict()

        for i in range(len(nums)):
            num = nums[i]
            miss = target - num
            missing_to_target[i] = miss

            if miss not in missing_to_target_pos:
                missing_to_target_pos[miss] = [i]
            else:
                missing_to_target_pos[miss].append(i)

        for i in range(len(missing_to_target)):
            miss = missing_to_target[i]
            goal = target - miss
            if goal not in missing_to_target_pos:
                continue
            positions = missing_to_target_pos[goal]
            
            for position in positions:
                if position == i:
                    continue

                if miss + missing_to_target[position] == target:
                    return [i, position]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
