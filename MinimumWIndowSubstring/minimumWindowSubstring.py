from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if not t or not s: return ""

        #contruct the dictionary
        charaDict = Counter(t)
        
        #define the left and right pointer, move the right point one each time, left as much as possible 
        left = 0
        right = 0

        #define the string that will be return, and start and end positin in the s. 
        start = 0
        end = 0

        #the require number of character in the return value, and check whether so far we find enough number character
        require_length = len(t)
        formed = 0

        while right<len(s):
            if s[right] in t:
                charaDict[s[right]] = charaDict[s[right]]-1
                if charaDict[s[right]]==0:
                    formed = formed+1
                
                while formed == require_length and left <= right:
                    # save the result 
                    end = right 
                    start = left
                    if s[left] in t and charaDict[s[left]]+1==0:
                        charaDict[s[left]] = charaDict[s[left]]+1
                        if charaDict[s[left]]==1:
                            formed = formed-1
                    left = left + 1

            right = right+1
            print("--------------------------------------------------")
            print("left and right is ")
            print(left)
            print(right)
            print(charaDict)
            print("formed equal: ")
            print(formed)
            print("start and end is ")
            print(start)
            print(end)
            print("--------------------------------------------------")

        if start==end and end == 0:
            return ""
        return s[start:end]



ob = Solution()
print("return value is " + ob.minWindow("ADOBECODEBANC", "ABC") + " end of value presentation")
