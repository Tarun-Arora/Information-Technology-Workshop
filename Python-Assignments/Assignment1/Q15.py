def remove(array,index):
    if(index>=len(array)):
        print("Item not present in this list")
    else:
        array.remove(array[index])
x=[i for i in input('\nEnter all elements of the array: ').split(' ')]
j=int(input('Enter index of element which is to be removed: '))
remove(x,j)
print("Resultant List\n",x)