s = "ababcbacadefegdehijhklij"

#output = "ababcbaca", "defegde", "hijhklij"
#define a dictionary
#{"character":#LastOfOccur}

stat = {}
count = 0
#generate the dictionary that record all character's last time occur
for char in s:
    stat[char]=count
    count+=1

#wrong case :  "caedbdedda"
record=[]
partition = 0
boundary = 0
for p in range(0, len(s)):
    partition+=1
    if stat[s[p]]==boundary and p==boundary:
        record.append(partition)
        partition = 0
        if p!=len(s)-1: boundary=stat[s[p+1]]
    
    if stat[s[p]]>boundary:
        boundary = stat[s[p]]


print(record)