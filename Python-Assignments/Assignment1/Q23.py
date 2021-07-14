arr1=[x for x in input('\nEnter the elements of  list1: ').split()]
arr2=[x for x in input('\nEnter the elements of  list2: ').split()]
print('List1\tList2')
for i in range(max(len(arr1),len(arr2))):
    if(i<len(arr1)):
        print(arr1[i],end='')
    print('',end='\t')
    if(i<len(arr2)):
        print(arr2[i],end='')
    print()
