from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if t==s: return t

        #contruct the dictionary
        d = dict(Counter(t))
        
        #define the left and right pointer, move the right point one each time, left as much as possible 
        slow = 0

        #define the string that will be return, and start and end positin in the s. 
        min_str = None
        min_length = len(s)+1

        #the require number of character in the return value, and check whether so far we find enough number character
        formed = 0

        for fast in range(len(s)):
            ch = s[fast]
            #skip if d[ch] doesn't matter, which means it is not in the string t 
            fast+=1
            if ch not in t:
                continue

            #use the ch to update d
            d[ch]-=1
            if d[ch]==0:
                formed+=1
            
            #if all character are atisfied, then need to move the left pointer
            while formed ==len(d) and slow <=fast:
                #save the result
                current_len = fast-slow
                if current_len < min_length:
                    min_length = current_len
                    min_str = s[slow:fast]

                #update the left boundary
                ch = s[slow]
                slow +=1
                if ch not in t:
                    continue
                d[ch]+= 1
                if d[ch]==1:
                    formed -=1
                
        return min_str if min_str is not None else ""



ob = Solution()
print("return value is " + ob.minWindow("ADOBECODEBANC", "ABC") + " end of value presentation")
