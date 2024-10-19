from typing import List

class Solution:
    def wordValue(self, word: str) -> tuple:
        result = [0] * 26
        baseValue = ord('a')

        for c in word:
            result[ord(c) - baseValue] += 1


        return tuple(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            wordValue = self.wordValue(word)

            if wordValue not in groups:
                groups[wordValue] = [word]
            else:
                groups[wordValue].append(word)

        return list(groups.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(["", 'ab', 'ba']))
# print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(['', '']))
# print(solution.groupAnagrams(['c', 'c']))
print(solution.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
