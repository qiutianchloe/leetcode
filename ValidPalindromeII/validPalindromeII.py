class Solution(object):
    def checkPalindrome(self, s, start, end):
        while(start<end):
            if s[start]!=s[end]:
                return False
            else:
                start = start+1
                end = end - 1
        return True


    def validPalindrome(self, s):
        start = 0
        end = len(s)-1
        while(start<end):
            if s[start] != s[end]:
                return self.checkPalindrome(s, start+1, end) or self.checkPalindrome(s, start, end-1)
            else:
                start=start+1
                end = end - 1
        return True

ob = Solution()
print("The result of aba, abca, abc")
print(ob.validPalindrome("abc"))
