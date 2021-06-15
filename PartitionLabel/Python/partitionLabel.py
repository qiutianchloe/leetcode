s = "ababcbacadefegdehijhklij"

#output = "ababcbaca", "defegde", "hijhklij"
#define a dictionary
#{"character":[#FirstOfOccur, #LastOfOccur]}

stat = {}
count = 0
for char in s:
    if char not in stat.keys():
        stat[char]=[count, count]
    else:
        stat[char][1]=count
    count+=1

#get all the interval(the first time and last timt a character occur) from dictionary
interval = stat.values()
#sort the list by first element ascending order
interval.sort(key=lambda x: x[0])

record = []
startOfBounday = interval[0][0]
endOfBounday = interval[0][1]


for i in range(1, len(interval)):

    if(interval[i][0]>endOfBounday):
        record.append([startOfBounday, endOfBounday])
        startOfBounday=interval[i][0]
        endOfBounday=interval[i][1]

    if(interval[i][0]<endOfBounday and interval[i][1]>endOfBounday):
        endOfBounday = interval[i][1]

record.append([startOfBounday, endOfBounday])

result = [record[i][1]-record[i][0]+1 for i in range(len(record))]
print(result)