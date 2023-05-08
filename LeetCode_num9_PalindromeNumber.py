class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]: # [::-1] makes the string with number reversed
            return True
        else:
            return False