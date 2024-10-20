from typing import List

import math

divCache = dict()
def div(a: int, b: int) -> int:
    if (a, b) in divCache:
        return divCache[(a, b)]

    numerator = abs(a)
    denominator = abs(b)
    result = 0

    for i in range(31, -1, -1):
        if denominator << i <= numerator:
            numerator -= denominator << i
            result |= 1 << i

    if (a < 0) ^ (b < 0):
        return -result

    divCache[(a, b)] = result
    return result

def productExceptZero(arr: List[int]) -> int:
    return math.prod(filter(lambda x: x != 0, arr))

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = productExceptZero(nums)
        zeroes = len(list(filter(lambda x: x == 0, nums)))

        if zeroes == 0:
            return [div(totalProduct, x) for x in nums]

        if zeroes == 1:
            return [totalProduct if num == 0 else 0 for num in nums]

        return [0] * len(nums)

# testProduct = productExceptZero([5,9,2,-9,-9,-7,-8,7,-9,10])
# print(abs(testProduct))
# print(testProduct / 5)
# print(div(testProduct, 5))

solution = Solution()
print(solution.productExceptSelf([9,0,-2]))

print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
print(solution.productExceptSelf([0, 0]))
print(solution.productExceptSelf([0,4,0]))
print(solution.productExceptSelf([5,9,2,-9,-9,-7,-8,7,-9,10]))