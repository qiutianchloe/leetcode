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
    
    def findLongestWord(self, s, dictionary):
        #check all the word if it is the substring of s
        qualified_words = []
        for word in dictionary:
            if self.checkSubstring(s, word):
                qualified_words.append(word)
        
        
        #check the results
        if len(qualified_words)==0: return ""
        if len(qualified_words)==1: return qualified_words[0]
        
        #find the largest word
        currentLen = len(qualified_words[0])
        currentWord = qualified_words[0]
        for i in range(1,len(qualified_words)):
            theLen = len(qualified_words[i])
            theWord = qualified_words[i]
            if theLen>currentLen:
                currentLen = theLen
                currentWord = theWord
            elif theLen==currentLen and theWord<currentWord:
                currentLen = theLen
                currentWord = theWord
        return currentWord
                
ob = Solution()
result = ob.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
print(result)