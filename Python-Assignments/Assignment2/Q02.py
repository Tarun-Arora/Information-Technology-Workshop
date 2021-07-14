from collections import defaultdict
list1=['Class-V','Class-VI','Class-VII','Class-VIII']
list2=[1,2,2,3]
d=defaultdict(set)
for i in range(len(list1)):
    d[list1[i]].add(list2[i])
print(d)
