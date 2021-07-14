arr=[x for x in input('\nEnter the elements of  list: ').split()]
n=int(input('Enter the value of n: '))
out=[]
for i in range(1,n+1):
    for j in arr:
        out.append(j+str(i))
print('Resultant List:\n',out,sep='')


