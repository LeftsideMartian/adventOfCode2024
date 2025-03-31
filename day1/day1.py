list1 = []
list2 = []

with open("day1.txt", "r") as f:
    for line in f:
        splitLine = line.split("   ")
        list1.append(int(splitLine[0]))
        list2.append(int(splitLine[1].strip("\n")))

list1.sort()
list2.sort()

totalDistance = 0

for i in range(len(list1)):
    totalDistance += abs(list1[i] - list2[i])

print(f"Total distance = {totalDistance}")

setOfList1 = set(list1)
similarityScore = 0
for item in setOfList1:
    similarityScore += item * list2.count(item)

print(f"Similarity score = {similarityScore}")

