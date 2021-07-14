union=set([])
difference=set([])
intersection=set([])
set1= set(["green", "blue"])
set2= set(["blue", "yellow"])
for i in set1:
    if i in set2:
        intersection.add(i)
    else:
        difference.add(i)
    union.add(i)
for i in set2:
    union.add(i)
print(f"Difference: {difference}, Union: {union}, Intersection: {intersection}")