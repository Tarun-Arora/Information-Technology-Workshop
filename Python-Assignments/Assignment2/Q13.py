l=[int(x) for x in input('Enter the sorted list of numbers: ').split()]
key=int(input('The number to search for: '))
st=0;en=len(l)-1
while(st<=en):
    mid=(st+en)//2
    if l[mid]==key:
        print(f"{key} was found at index {mid}")
        exit()
    elif l[mid]<key:
        st=mid+1
    else:
        en=mid-1
print(f'{key} not found in this list.')