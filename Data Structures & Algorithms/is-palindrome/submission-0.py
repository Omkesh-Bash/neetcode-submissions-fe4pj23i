import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = string.ascii_letters + string.digits
        s = s.lower()
        s = [s for s in s if s in alphanumeric ]
        return s == s[::-1]