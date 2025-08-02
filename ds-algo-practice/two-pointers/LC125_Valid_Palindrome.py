class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        return s == s[::-1]
