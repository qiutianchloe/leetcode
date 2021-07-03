#LongestWordinDictionarythroughDeleting
class Solution(object):
    def checkSubstring(self, s, t):
        if(len(t)>len(s)): return False
        m, n, find=0, len(t), 0
        for i in range(0, n):
            ch = t[i]
            while m<len(s):
                if ch==s[m]:
                    find+=1
                    m+=1
                    break
                m+=1
        if find<n:
            return False
        return True
    
    def numMatchingSubseq(self, s, dictionary):
        #check all the word if it is the substring of s
        qualified_words = []
        for word in dictionary:
            if self.checkSubstring(s, word):
                qualified_words.append(word)
        return len(qualified_words)

ob = Solution()
result = ob.numMatchingSubseq("abcde",["a","bb","acd","ace"])
print(result)