class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredLetters = ''.join(filter(lambda c: c.isalpha() or c.isdigit(), s)).lower()

        stack = [c for c in filteredLetters]

        for c in filteredLetters:
            top = stack.pop()
            if c != top:
                return False

        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))
