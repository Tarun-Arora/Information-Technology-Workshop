l=[int(x) for x in input('Enter a list of integers you want to sort: ').split()]
def selectionSort(l):
    for top in range(len(l)-1):
        k=top
        for i in range(top+1,len(l)):
            if l[i]<l[k]:
                k=i
        l[top],l[k]=l[k],l[top]
print('The given list to be sorted is:',l)
selectionSort(l)
print('The sorted list is:',l)