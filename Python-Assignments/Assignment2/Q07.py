count=0
l=[10,20,30,(10,20),40]
for i in l:
    if type(i)==tuple:
        break
    count+=1
print(count)