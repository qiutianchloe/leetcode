class Solution(object):
    def numMatchingSubseq(self, s, words):
        import bisect
        def MatchedSub(word):
            l = -1
            for ch in word:
                #find the ch first exist in the list 
                leftmostpos = bisect.bisect_left(pos[ch], l+1)
                if leftmostpos==len(pos[ch]) : return 0
                l = pos[ch][leftmostpos]
            return 1

        #create a dictionary record all the character's position in tht strin
        #initialize the structure
        pos={chr(i+ord('a')) : [] for i in range(26)}
        #record the character
        for index, ch in enumerate(s):pos[ch].append(index)

        return sum(map(MatchedSub, words))
        

        


ob = Solution()
result = ob.numMatchingSubseq("abcde",["a","bb","acd","ace"])
print(result)