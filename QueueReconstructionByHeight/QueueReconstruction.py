people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

#sort by height :[[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]
people.sort(key=lambda x: (-x[0], x[1]))

result = []

for i in range(len(people)):
    result.insert(people[i][1], people[i]); 

print(result)
