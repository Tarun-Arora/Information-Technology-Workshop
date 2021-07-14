l=[int(x) for x in input('Enter a list of integers you want to sort: ').split()]
def mergeSort(l,st,en):
    if(st>=en):
        return
    mid=(st+en)//2
    mergeSort(l,st,mid);mergeSort(l,mid+1,en)
    merge(l,st,en)
def merge(l,st,en):
    mid=(st+en)//2
    left=l[st:(mid+1)];right=l[(mid+1):en+1]
    i=0;j=0;k=st
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            l[k]=right[j]
            k+=1;j+=1
        else:
            l[k]=left[i]
            k+=1;i+=1
    while i<len(left):
        l[k]=left[i]
        k+=1;i+=1
    while j<len(right):
        l[k]=right[j]
        k+=1;j+=1
print('The given list to be sorted is:',l)
mergeSort(l,0,len(l)-1)
print('The sorted list is:',l)