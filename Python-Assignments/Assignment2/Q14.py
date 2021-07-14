l=[int(x) for x in input('Enter a list of integers you want to sort: ').split()]
def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
print('The given list to be sorted is:',l)
bubbleSort(l)
print('The sorted list is:',l)