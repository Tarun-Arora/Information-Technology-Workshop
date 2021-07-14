arr=[x for x in input("\nEnter a List: ").split(' ')]
s=input('Enter the string to be inserted at the start of every element: ')
for i in range(len(arr)):
    arr[i]=s+arr[i]
print('Resultant String:\n',arr,sep='')