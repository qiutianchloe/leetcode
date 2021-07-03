class Solution(object):
    def numMatchingSubseq(self, s, words):
        def MatchedSub(word):
            i = 0
            for ch in word:
                i = next[i][ord(ch)-ord('a')]
                if i==-1:return 0
            return 1


        next = [[-1 for i in range(26)] for j in range(len(s)+1)]
        m = len(s)
        s = "#"+s
        while(m>0):
            for k in range(26):
                next[m-1][k] = next[m][k]
            next[m-1][ord(s[m])-ord('a')]=m
            m=m-1

        return sum(map(MatchedSub, words))


ob = Solution()
result = ob.numMatchingSubseq("abcde",["a","bb","acd","ace"])
print(result)