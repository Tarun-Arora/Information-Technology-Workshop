data=open('test.txt','r')
v=[]
for i in data.readlines():
    v.append(tuple(i.split()))
i=0
while i<len(v):
    if(len(v[i])==0):
        v.pop(i)
    else:
        i+=1
print(v)
data.close()