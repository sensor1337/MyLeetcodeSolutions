class Solution:
    def romanToInt(self, s: str) -> int:
        # create a vocabulary with roman numerals' int symbols
        romanvb = {
            "I" : 1,
            "V" : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans = 0 # output num
        for i in range(len(s) - 1): # range is less on 1 as we'll add the last symbol later
            if romanvb[s[i]] < romanvb[s[i+1]]: # if i < i-1 it means that we have to subtract it
                ans -= romanvb[s[i]]
            else:
                ans += romanvb[s[i]] # else just add the num in total value
        return ans + romanvb[s[-1]] # output num + last symbol as it can't be subtracted, we have nowhere from