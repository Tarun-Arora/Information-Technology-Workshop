inp=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
max=0;maxSum=0
for i in range(len(inp)):
    sum=0
    for j in inp[i]:
        sum+=j
    if(sum>maxSum):
        maxSum=sum
        max=i
print("The Original List is:\n",inp,sep='')
print("The List with maximum sum is:\n",inp[max],sep='')