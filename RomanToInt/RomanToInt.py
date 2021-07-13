class Solution(object):
    def romanToInt(self, s):
        #hash Table to record all the values 
        romanToInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)-1,-1,-1):
            num = romanToInt[s[i]]
            if 4 * num < ans: ans -= num
            else: ans += num
        return ans
    
ob = Solution()
result = ob.romanToInt("III")
print(result)