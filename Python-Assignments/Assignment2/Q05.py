l=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for i in range(len(l)-1,-1,-1):
    if len(l[i])==0:
        del l[i]
print(l)