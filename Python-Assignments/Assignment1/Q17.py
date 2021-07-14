x= [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print('\nOriginal List:\n',x,sep='')
res=[]
for i in x:
    if i not in res:
        res.append(i)
print('Resultant List:\n',res,sep='')
