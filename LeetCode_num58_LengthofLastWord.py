class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] !=' ':
                out += 1
            elif out:
                return out
        return out