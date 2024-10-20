from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] = frequency[num] + 1

        items = list(frequency.items())
        items.sort(key = lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(items[i][0])

        return result


solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([-1,-1], 1))